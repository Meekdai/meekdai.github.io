MJPG-streamer是一个优秀的开源项目，它可以通过HTTP的方式访问linux上面的兼容摄像头，从而做到远程视频传输的效果。本文主要记录树莓派4B配置的过程。

我使用的树莓派是4B 2G内存版本，运行的是`Raspberry Pi OS Lite(32-bit) 2023-05-03`版本的系统。

启动树莓派后，插入USB摄像头，可以通过`lsusb`和`ls /dev/video*` 查看USB摄像头有没有被正确挂载。

### 安装库
然后是下面必须要安装的库，特别注意`libjpeg9-dev`，网上的一些教程都是安装`libjpeg8-dev`

```
sudo apt-get update
sudo apt-get install subversion
sudo apt-get install libjpeg9-dev
sudo apt-get install imagemagick
sudo apt-get install libv4l-dev
sudo apt-get install cmake
```

### 克隆编译

```
sudo git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make all
sudo make install
```
如果由于网络问题无法克隆的，可以直接下载`zip`包，然后解压安装
```
unzip mjpg-streamer-master.zip
cd mjpg-streamer/mjpg-streamer-experimental
make all
sudo make install
```

### 运行

如下指令中`/dev/video0`是对应的摄像头，`8080`是网页访问的端口号
```
mjpg_streamer -i "input_uvc.so -d /dev/video0 -n -f 10 -r 1280x720" -o "output_http.so -p 8080 -w www"
```
然后在浏览器中访问`http://[树莓派ip]:8080`就可以看到摄像头的画面了，里面还有一些配置就不多展开了。

### 配置多摄像头
```
mjpg_streamer -i "input_uvc.so -d /dev/video0 -n -f 10 -r 1280x720" -o "output_http.so -p 8080 -w www" & mjpg_streamer -i "input_uvc.so -d /dev/video2 -n -f 10 -r 1280x720" -o "output_http.so -p 8082 -w www"
```
如此，访问`8080`端口和`8082`端口就是两个不同的摄像头了，增加多个摄像头同理。

### 其他

***fswebcam***
通过安装`sudo apt-get install fswebcam`，然后`fswebcam --no-banner -r 640*480 camera.jpg` 可以在`/home/pi`目录下生成一个当前摄像头拍摄到的实时照片。以此证明USB摄像头工作正常。

***motion***
可参考：https://bun.plus/posts/monitoring-with-raspberry-pi-and-motion

***restreamer***
可参考：https://docs.datarhei.com/restreamer/getting-started/quick-start

试用`motion`和`restreamer`都出现视频卡顿的问题，不知道是不是我没有配置对，但是`MJPG-streamer`是真的开箱即用，很方便。

<!-- ##{"script":"<script src='https://blog.meekdai.com/assets/GmeekTOC.js'></script>"}## -->