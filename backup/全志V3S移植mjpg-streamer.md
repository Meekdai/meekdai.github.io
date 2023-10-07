上一篇文章在树莓派上简单的测试了一下USB摄像头通过mjpg-streamer推流的步骤，本篇记录使用全志的V3S替代树莓派实现这个功能。由于树莓派上有包管理工具，所以可以直接使用`apt-get`指令来安装需要的软件脚本，但是V3S没有包管理，需要自己移植并且交叉编译。

### 开发环境
开发板：荔枝派zero
buildroot：2018.08.2
FLASH：32M
编译环境：WIN10 WSL 和 Github Codepaces

具体参考：[V3s buildroot 一键生成打包生成32M spi flash 镜像, jffs2 文件系统, 默认启动 Qt 模拟时钟demo,](https://whycan.com/t_2169.html)

### 开启UVC摄像头
进入`linux-zero-4.13.y`目录，可通过`make menuconfig`启用，也可以直接编辑`.config`文件，主要是启用 `UVC` 和 `V4L2`  

具体参考1：[嵌入式Linux平台下的UVC驱动和V4L2](https://ccclaire.com/index.php/2021/03/25/camera-driver-in-embbedlinux-and-v4l2/)  
具体参考2：[关于V3S使用usb摄像头的问题](https://whycan.com/t_6234.html)  
具体参考3：[V3S插入USB设备没有反应](https://whycan.com/t_7459.html)  
具体参考4：[荔枝派Zero(全志V3S)驱动开发之USB摄像头](https://cloud.tencent.com/developer/article/2311086)  

### 交叉编译mjpg-streamer
#### libjpeg库安装

1. 下载 [jpegsrc.v9d.tar.gz](http://www.ijg.org/files/jpegsrc.v9d.tar.gz) 
2. 解压 `tar -vxzf jpegsrc.v9d.tar.gz`
3. 配置 `./configure CC=/mnt/d/MICROPYTHON/V3S/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc --prefix=$PWD/_install --host=arm-linux-gnueabihf`
4. 编译 `make`
5. 安装 `make install`

#### mjpg-streamer编译

1. 下载[https://sourceforge.net/p/mjpg-streamer/code/HEAD/tree/](https://sourceforge.net/p/mjpg-streamer/code/HEAD/tree/)
2. 进入mjpg-streamer目录，修改`makefile`中的`CC=gcc`为自己的编译器地址，包括使用了的`plugins`目录下的所有`makefile`文件。
```makefile
CC=/mnt/d/MICROPYTHON/V3S/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc
```

3. 根据需要编译下面的插件
```makefile
# define the names and targets of the plugins
PLUGINS = input_uvc.so
PLUGINS += output_file.so
PLUGINS += output_udp.so
PLUGINS += output_http.so
PLUGINS += input_testpicture.so
#PLUGINS += output_autofocus.so
#PLUGINS += input_gspcav1.so
PLUGINS += input_file.so
PLUGINS += output_rtsp.so
# PLUGINS += output_ptp2.so # commented out because it depends on libgphoto
# PLUGINS += input_control.so # commented out because the output_http does it's job
# PLUGINS += input_http.so 
# PLUGINS += output_viewer.so # commented out because it depends on SDL
```

4. UVC模块依赖之前编译的jpeg库，所以在plugins/input_uvc/Makefile中指定之前编译的库和头文件(注意替换路径)：
```makefile
CFLAGS += -I/mnt/c/Users/Meekdai/Desktop/v3s/app/jpeg-9d/_install/include
CFLAGS += -L/mnt/c/Users/Meekdai/Desktop/v3s/app/jpeg-9d/_install/lib
```

5. 然后执行`make`编译，结束后拷贝文件到`V3S`中：
```
jpeg-9d/_install 的/lib/下的库文件拷贝到开发板的/lib/目录下
*.so 文件拷贝到开发板的/lib/目录下
mjpg_streamer 文件拷贝到开发板的/bin/目录下
www 文件夹拷贝到/opt/目录下
```

### 运行mjpg-streamer

```
mjpg_streamer -i "input_uvc.so -d /dev/video0 -n -f 10 -r 1280x720" -o "output_http.so -p 8080 -w /opt/www"
```

如果报权限的错误，则 `cd` 到 `/bin/` 目录下，执行 `chmod 777 mjpg_streamer`  
然后访问：[http://192.168.10.35:8080](http://192.168.10.35:8080)  

### 其他

1. 使能以太网（4.13-y版本）

```
#打开网络
ifconfig eth0 up
#设置ip:
ifconfig eth0 192.168.10.35
#设置网关
route add default gw 192.168.10.1
```

2. 查看USB设备和摄像头
```
lsusb
ls /dev/video*
```

3. 报错`Unsupported relocation type: R_X86_64_PLT32 (4)` 解决方案：[x86: Treat R_X86_64_PLT32 as R_X86_64_PC32](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b21ebf2fb4cde1618915a97cc773e287ff49173e)





