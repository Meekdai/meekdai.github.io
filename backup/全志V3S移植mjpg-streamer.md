上一篇文章在树莓派上简单的测试了一下USB摄像头通过mjpg-streamer推流的步骤，本篇记录使用全志的V3S替代树莓派实现这个功能。由于树莓派上有包管理工具，所以可以直接使用`apt-get`指令来安装需要的软件脚本，但是V3S没有包管理，需要自己移植并且交叉编译。

### 一、开发环境
开发板：荔枝派zero  
buildroot：2018.08.2  
FLASH：32M  
编译环境：WIN10 WSL 和 Github Codepaces  

具体参考：[V3s buildroot 一键生成打包生成32M spi flash 镜像, jffs2 文件系统, 默认启动 Qt 模拟时钟demo,](https://whycan.com/t_2169.html)

### 二、开启UVC摄像头
进入`linux-zero-4.13.y`目录，可通过`make menuconfig`启用，也可以直接编辑`.config`文件，主要是启用 `UVC` 和 `V4L2`  

具体参考1：[嵌入式Linux平台下的UVC驱动和V4L2](https://ccclaire.com/index.php/2021/03/25/camera-driver-in-embbedlinux-and-v4l2/)  
具体参考2：[关于V3S使用usb摄像头的问题](https://whycan.com/t_6234.html)  
具体参考3：[V3S插入USB设备没有反应](https://whycan.com/t_7459.html)  
具体参考4：[荔枝派Zero(全志V3S)驱动开发之USB摄像头](https://cloud.tencent.com/developer/article/2311086)  
具体参考5：[Linux UVC driver and tools](http://www.ideasonboard.org/uvc/)  
具体参考6：[荔枝派Zero(全志V3S)驱动开发之USB摄像头 1](https://developer.aliyun.com/article/1337927?spm=a2c6h.12873639.article-detail.21.43c72ffcUlekZP)  

### 三、交叉编译mjpg-streamer
#### libjpeg库安装

1. 下载 [jpegsrc.v9e.tar.gz](http://www.ijg.org/files/jpegsrc.v9e.tar.gz) 
2. 解压 `tar -vxzf jpegsrc.v9e.tar.gz`
3. 配置 `./configure CC=/mnt/d/MICROPYTHON/V3S/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc --prefix=$PWD/_install --host=arm-linux-gnueabihf --enable-shared --enable-static`
4. 编译 `make`
5. 安装 `make install`

#### mjpg-streamer编译

1. 下载 [https://sourceforge.net/p/mjpg-streamer/code/HEAD/tree/](https://sourceforge.net/p/mjpg-streamer/code/HEAD/tree/)
2. 进入mjpg-streamer目录，修改`plugins`目录下的`makefile`文件，指向自己的路径。

```
# CFLAGS += -O1 -DLINUX -D_GNU_SOURCE -Wall -shared -fPIC
CFLAGS += -O1 -DLINUX -D_GNU_SOURCE -Wall -shared -fPIC -I /mnt/c/Users/Meekdai/Desktop/v3s/app/tools/jpeg-9e/_install/include
```

```
input_uvc.so: $(OTHER_HEADERS) input_uvc.c v4l2uvc.lo jpeg_utils.lo dynctrl.lo
	$(CC) $(CFLAGS) -L /mnt/c/Users/Meekdai/Desktop/v3s/app/tools/jpeg-9e/_install/lib -o $@ input_uvc.c v4l2uvc.lo jpeg_utils.lo dynctrl.lo $(LFLAGS)
```

3. 根据需要编译下面的插件，内容在主Makefile里。

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

4. 然后执行`make CC=/mnt/d/MICROPYTHON/V3S/gcc-linaro-6.3.1-2017.02-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc`编译，结束后拷贝文件到`V3S`中：

```
jpeg-9d/_install 的/lib/下的库文件拷贝到开发板的/lib/目录下
*.so 文件拷贝到开发板的/lib/目录下
mjpg_streamer 文件拷贝到开发板的/bin/目录下
www 文件夹拷贝到/opt/目录下
```

具体参考1：[荔枝派Zero(全志V3S)驱动开发之RGB LCD屏幕显示jpg图片](https://blog.csdn.net/qq_41839588/article/details/130598083?spm=a2c6h.12873639.article-detail.7.43c72ffcUlekZP)  
具体参考2：[荔枝派Zero(全志V3S)驱动开发之USB摄像头 2](https://developer.aliyun.com/article/1337930?spm=a2c6h.12873639.article-detail.20.44d318445QdBXC)  
具体参考3：[mjpeg-streamer交叉编译](https://blog.csdn.net/sy84436446/article/details/108627453)   

### 四、运行mjpg-streamer

```
mjpg_streamer -i "input_uvc.so -d /dev/video0 -n -f 10 -r 1280x720 -yuv" -o "output_http.so -p 8080 -w /opt/www"
```

如果报权限的错误，执行 `chmod 777 /bin/mjpg_streamer`  
然后访问：[http://192.168.10.35:8080](http://192.168.10.35:8080)  

### 五、其他

1. 使能以太网（4.13-y版本）

```
#打开网络
#设置ip
#设置网关

ifconfig eth0 up
ifconfig eth0 192.168.10.35
route add default gw 192.168.10.1
```

2. 查看USB设备和摄像头
```
lsusb
ls /dev/video*
```

3. 报错`Unsupported relocation type: R_X86_64_PLT32 (4)` 解决方案：[x86: Treat R_X86_64_PLT32 as R_X86_64_PC32](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b21ebf2fb4cde1618915a97cc773e287ff49173e)

4. 编译指令
```
#解压
tar xvf  backup_20190220A.tgz

#执行一次 make (约2小时)
make

#再次解压覆盖文件, 编译(约5分钟)
sh ./pre_build.sh
make

#打包
sh ./pack.sh

```



