USB摄像头有一个全平台统一的BUG，就是2个或者多个USB摄像头插在同一个USB总线上，即使用USB-HUB扩展的口，会出现第二个摄像头无法打开的情况。目前一个项目需要在V3S上启用2个USB摄像头，就遇到了麻烦，同时也解决了上一篇文章只有`YUV`格式才能输出 `mjpg-streamer` 的BUG。

### 填坑
先把上一篇文章的坑先解决了，由于之前很少搞`buildroot`相关的东西，所以开始的时候就在谷歌上查阅了很多资料，正是这些资料让我进入了这么一个大坑（不过也学到了很多）。坑：`mjpg-streamer` 需要单独交叉编译然后拷贝进嵌入式板子是唯一的解决办法。

其实使用 `buildroot` 根本不需要再单独下载源代码/配置/编译等，直接 `make menuconfig` 在里面启用 `mjpg-streamer` 和 `libjpeg` 就可以了（Target packages > Networking applications）~~~我真是个大冤种。

体现在 `.config` 文件中就是修改这么几句代码：
```
BR2_PACKAGE_MJPG_STREAMER=y

BR2_PACKAGE_JPEG=y
BR2_PACKAGE_LIBJPEG=y
BR2_PACKAGE_PROVIDES_JPEG="libjpeg"
```

### 启用多摄像头

启用第二个摄像头报错如下：

```
VIDIOC_STREAMON: No space left on device
```

网上有这样的解决方式：
```
# 减低帧率和分辨率
```

还有这样的：

```
sudo rmmod uvcvideo
sudo modprobe uvcvideo quirks=128
```

对于我来说，下面这个实测有效：

```
# 修改内核源码，在buildroot的目录下面就是这个路径文件
output\build\linux-zero-4.13.y\drivers\media\usb\uvc\uvc_video.c

# 找到这个文件中的函数 uvc_fixup_video_ctrl

# 在这个函数的最后添加一行代码
if(format->flags & UVC_FMT_FLAG_COMPRESSED){ctrl->dwMaxPayloadTransferSize = 0x400;}

```

为了更加清晰，下面是修改后的 `uvc_fixup_video_ctrl` 代码

```
static void uvc_fixup_video_ctrl(struct uvc_streaming *stream,
	struct uvc_streaming_control *ctrl)
{
	struct uvc_format *format = NULL;
	struct uvc_frame *frame = NULL;
	unsigned int i;

	for (i = 0; i < stream->nformats; ++i) {
		if (stream->format[i].index == ctrl->bFormatIndex) {
			format = &stream->format[i];
			break;
		}
	}

	if (format == NULL)
		return;

	for (i = 0; i < format->nframes; ++i) {
		if (format->frame[i].bFrameIndex == ctrl->bFrameIndex) {
			frame = &format->frame[i];
			break;
		}
	}

	if (frame == NULL)
		return;

	if (!(format->flags & UVC_FMT_FLAG_COMPRESSED) ||
	     (ctrl->dwMaxVideoFrameSize == 0 &&
	      stream->dev->uvc_version < 0x0110))
		ctrl->dwMaxVideoFrameSize =
			frame->dwMaxVideoFrameBufferSize;

	/* The "TOSHIBA Web Camera - 5M" Chicony device (04f2:b50b) seems to
	 * compute the bandwidth on 16 bits and erroneously sign-extend it to
	 * 32 bits, resulting in a huge bandwidth value. Detect and fix that
	 * condition by setting the 16 MSBs to 0 when they're all equal to 1.
	 */
	if ((ctrl->dwMaxPayloadTransferSize & 0xffff0000) == 0xffff0000)
		ctrl->dwMaxPayloadTransferSize &= ~0xffff0000;

	if (!(format->flags & UVC_FMT_FLAG_COMPRESSED) &&
	    stream->dev->quirks & UVC_QUIRK_FIX_BANDWIDTH &&
	    stream->intf->num_altsetting > 1) {
		u32 interval;
		u32 bandwidth;

		interval = (ctrl->dwFrameInterval > 100000)
			 ? ctrl->dwFrameInterval
			 : frame->dwFrameInterval[0];

		/* Compute a bandwidth estimation by multiplying the frame
		 * size by the number of video frames per second, divide the
		 * result by the number of USB frames (or micro-frames for
		 * high-speed devices) per second and add the UVC header size
		 * (assumed to be 12 bytes long).
		 */
		bandwidth = frame->wWidth * frame->wHeight / 8 * format->bpp;
		bandwidth *= 10000000 / interval + 1;
		bandwidth /= 1000;
		if (stream->dev->udev->speed == USB_SPEED_HIGH)
			bandwidth /= 8;
		bandwidth += 12;

		/* The bandwidth estimate is too low for many cameras. Don't use
		 * maximum packet sizes lower than 1024 bytes to try and work
		 * around the problem. According to measurements done on two
		 * different camera models, the value is high enough to get most
		 * resolutions working while not preventing two simultaneous
		 * VGA streams at 15 fps.
		 */
		bandwidth = max_t(u32, bandwidth, 1024);

		ctrl->dwMaxPayloadTransferSize = bandwidth;
	}
	if(format->flags & UVC_FMT_FLAG_COMPRESSED){ctrl->dwMaxPayloadTransferSize = 0x400;}//meekdai
}
```

重新编译好代码下载固件后，执行下面的代码就可以用2个摄像头以MJPEG格式推流了。
```
mjpg_streamer -i "input_uvc.so -d /dev/video0 -f 10 -n -r 1920x1080" -o "output_http.so -p 8080 -w /usr/www" & mjpg_streamer -i "input_uvc.so -d /dev/video1 -f 10 -n -r 1920x1080" -o "output_http.so -p 8081 -w /usr/www"
```

