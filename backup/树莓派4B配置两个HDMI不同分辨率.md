在树莓派4之前，都是一个HDMI接口，所以没有这个问题。而树莓派4B有2个HDMI接口，可以输出双4K。

在树莓派根目录下有一个文件`config.txt`,我们需要修改里面的参数。

下面的配置为HDMI0输出`1080P 60Hz`，HDMI1输出`1024*768 60Hz`。

```python
[HDMI:0]
  hdmi_group=2
  hdmi_mode=82
[HDMI:1]
  hdmi_group=2
  hdmi_mode=16
```

`hdmi_group=1`代表`CEA`模式（电视规格分辨率，不包含音频，通常使用DVI接口）

`hdmi_group=2`则代表`DMT`模式（计算机显示器分辨率，包含音频，通常使用HDMI接口）

hdmi_mode参数表可以参考下面：

[tabs]
[tab name="hdmi_group=1 (CEA)"]
| hdmi_mode | Resolution | Frequency | Screen Aspect | Notes |
| ---- | ---- | ---- | ---- | ---- |
| 1 | VGA (640x480) | 60Hz | 4:3 |  |
| 2 | 480p | 60Hz | 4:3 |  |
| 3 | 480p | 60Hz | 16:9 |  |
| 4 | 720p | 60Hz | 16:9 |  | 
| 5 | 1080i | 60Hz | 16:9 | |
| 6 | 480i  | 60Hz | 4:3 | |
| 7 | 480i  | 60Hz | 16:9 | |
| 8 | 240p  | 60Hz | 4:3 | |
| 9 | 240p  | 60Hz | 16:9 | |
| 10 | 480i | 60Hz | 4:3 | pixel quadrupling |
| 11 | 480i | 60Hz | 16:9 | pixel quadrupling |
| 12 | 240p | 60Hz | 4:3 | pixel quadrupling |
| 13 | 240p | 60Hz | 16:9 | pixel quadrupling |
| 14 | 480p | 60Hz | 4:3 | pixel doubling |
| 15 | 480p | 60Hz | 16:9 | pixel doubling |
| 16 | 1080p | 60Hz | 16:9 | |
| 17 | 576p | 50Hz | 4:3 | |
| 18 | 576p | 50Hz | 16:9 | |
| 19 | 720p | 50Hz | 16:9 | |
| 20 | 1080i | 50Hz | 16:9 | |
| 21 | 576i | 50Hz | 4:3 | |
| 22 | 576i | 50Hz | 16:9 | |
| 23 | 288p | 50Hz | 4:3 | |
| 24 | 288p | 50Hz | 16:9 | |
| 25 | 576i | 50Hz | 4:3 | pixel quadrupling |
| 26 | 576i | 50Hz | 16:9 | pixel quadrupling |
| 27 | 288p | 50Hz | 4:3 | pixel quadrupling |
| 28 | 288p | 50Hz | 16:9 | pixel quadrupling |
| 29 | 576p | 50Hz | 4:3 | pixel doubling |
| 30 | 576p | 50Hz | 16:9 | pixel doubling |
| 31 | 1080p | 50Hz | 16:9 | |
| 32 | 1080p | 24Hz | 16:9 | |
| 33 | 1080p | 25Hz | 16:9 | |
| 34 | 1080p | 30Hz | 16:9 | |
| 35 | 480p | 60Hz | 4:3 | pixel quadrupling |
| 36 | 480p | 60Hz | 16:9 | pixel quadrupling |
| 37 | 576p | 50Hz | 4:3 | pixel quadrupling |
| 38 | 576p | 50Hz | 16:9 | pixel quadrupling |
| 39 | 1080i | 50Hz | 16:9 | reduced blanking |
| 40 | 1080i | 100Hz | 16:9 | |
| 41 | 720p | 100Hz | 16:9 | |
| 42 | 576p | 100Hz | 4:3 | |
| 43 | 576p | 100Hz | 16:9 | |
| 44 | 576i | 100Hz | 4:3 | |
| 45 | 576i | 100Hz | 16:9 | |
| 46 | 1080i | 120Hz | 16:9 | |
| 47 | 720p | 120Hz | 16:9 | |
| 48 | 480p | 120Hz | 4:3 | |
| 49 | 480p | 120Hz | 16:9 | |
| 50 | 480i | 120Hz | 4:3 | |
| 51 | 480i | 120Hz | 16:9 | |
| 52 | 576p | 200Hz | 4:3 | |
| 53 | 576p | 200Hz | 16:9 | |
| 54 | 576i | 200Hz | 4:3 | |
| 55 | 576i | 200Hz | 16:9 | |
| 56 | 480p | 240Hz | 4:3 | |
| 57 | 480p | 240Hz | 16:9 | |
| 58 | 480i | 240Hz | 4:3 | |
| 59 | 480i | 240Hz | 16:9 | |
| 60 | 720p | 24Hz | 16:9 | |
| 61 | 720p | 25Hz | 16:9 | |
| 62 | 720p | 30Hz | 16:9 | |
| 63 | 1080p | 120Hz | 16:9 | |
| 64 | 1080p | 100Hz | 16:9 | |
| 65 | Custom | | |  
| 66 | 720p | 25Hz | 64:27 Pi 4 |
| 67 | 720p | 30Hz | 64:27 Pi 4 |
| 68 | 720p | 50Hz | 64:27 Pi 4 |
| 69 | 720p | 60Hz | 64:27 Pi 4 |
| 70 | 720p | 100Hz | 64:27 Pi 4 |
| 71 | 720p | 120Hz | 64:27 Pi 4 |
| 72 | 1080p | 24Hz | 64:27 Pi 4 |
| 73 | 1080p | 25Hz | 64:27 Pi 4 |
| 74 | 1080p | 30Hz | 64:27 Pi 4 |
| 75 | 1080p | 50Hz | 64:27 Pi 4 |
| 76 | 1080p | 60Hz | 64:27 Pi 4 |
| 77 | 1080p | 100Hz | 64:27 Pi 4 |
| 78 | 1080p | 120Hz | 64:27 Pi 4 |
| 79 | 1680x720 | 24Hz | 64:27 Pi 4 |
| 80 | 1680x720 | 25Hz | 64:27 Pi 4 |
| 81 | 1680x720 | 30Hz | 64:27 | Pi 4 |
| 82 | 1680x720 | 50Hz | 64:27 | Pi 4 |
| 83 | 1680x720 | 60Hz | 64:27 | Pi 4 |
| 84 | 1680x720 | 100Hz | 64:27 | Pi 4 |
| 85 | 1680x720 | 120Hz | 64:27 | Pi 4 |
| 86 | 2560x720 | 24Hz | 64:27 | Pi 4 |
| 87 | 2560x720 | 25Hz | 64:27 | Pi 4 |
| 88 | 2560x720 | 30Hz | 64:27 | Pi 4 |
| 89 | 2560x720 | 50Hz | 64:27 | Pi 4 |
| 90 | 2560x720 | 60Hz | 64:27 | Pi 4 |
| 91 | 2560x720 | 100Hz | 64:27 | Pi 4 |
| 92 | 2560x720 | 120Hz | 64:27 | Pi 4 |
| 93 | 2160p | 24Hz | 16:9 | Pi 4 |
| 94 | 2160p | 25Hz | 16:9 | Pi 4 |
| 95 | 2160p | 30Hz | 16:9 | Pi 4 |
| 96 | 2160p | 50Hz | 16:9 | Pi 4 |
| 97 | 2160p | 60Hz | 16:9 | Pi 4 |
| 98 | 4096x2160 | 24Hz | 256:135 | Pi 4 |
| 99 | 4096x2160 | 25Hz | 256:135 | Pi 4 |
| 100 | 4096x2160 | 30Hz | 256:135 | Pi 4 |
| 101 | 4096x2160 | 50Hz | 256:135 | Pi 4 |
| 102 | 4096x2160 | 60Hz | 256:135 | Pi 4 |
| 103 | 2160p | 24Hz | 64:27 | Pi 4 |
| 104 | 2160p | 25Hz | 64:27 | Pi 4 |
| 105 | 2160p | 30Hz | 64:27 | Pi 4 |
| 106 | 2160p | 50Hz | 64:27 | Pi 4 |
| 107 | 2160p | 60Hz | 64:27 | Pi 4 |

[/tab]

[tab name="hdmi_group=2 (DMT)"]
| hdmi_mode | Resolution | Frequency | Screen Aspect | Notes |
| ---- | ---- | ---- | ---- | ---- |
| 1 | 640x350 | 85Hz | | |
| 2 | 640x400 | 85Hz | 16:10 | |
| 3 | 720x400 | 85Hz | | |
| 4 | 640x480 | 60Hz | 4:3 | |
| 5 | 640x480 | 72Hz | 4:3 | |
| 6 | 640x480 | 75Hz | 4:3 | |
| 7 | 640x480 | 85Hz | 4:3 | |
| 8 | 800x600 | 56Hz | 4:3 | |
| 9 | 800x600 | 60Hz | 4:3 | |
| 10 | 800x600 | 72Hz | 4:3 | |
| 11 | 800x600 | 75Hz | 4:3 | |
| 12 | 800x600 | 85Hz | 4:3 | |
| 13 | 800x600 | 120Hz | 4:3 | |
| 14 | 848x480 | 60Hz | 16:9 | |
| 15 | 1024x768 | 43Hz | 4:3 | incompatible with the Raspberry Pi |
| 16 | 1024x768 | 60Hz | 4:3 | |
| 17 | 1024x768 | 70Hz | 4:3 | |
| 18 | 1024x768 | 75Hz | 4:3 | |
| 19 | 1024x768 | 85Hz | 4:3 | |
| 20 | 1024x768 | 120Hz | 4:3 | |
| 21 | 1152x864 | 75Hz | 4:3 | |
| 22 | 1280x768 | 60Hz | 15:9 | reduced blanking |
| 23 | 1280x768 | 60Hz | 15:9 | |
| 24 | 1280x768 | 75Hz | 15:9 | |
| 25 | 1280x768 | 85Hz | 15:9 | |
| 26 | 1280x768 | 120Hz | 15:9 | reduced blanking |
| 27 | 1280x800 | 60Hz | 16:10 | reduced blanking |
| 28 | 1280x800 | 60Hz | 16:10 | |
| 29 | 1280x800 | 75Hz | 16:10 | |
| 30 | 1280x800 | 85Hz | 16:10 | |
| 31 | 1280x800 | 120Hz | 16:10 | reduced blanking |
| 32 | 1280x960 | 60Hz | 4:3 | |
| 33 | 1280x960 | 85Hz | 4:3 | |
| 34 | 1280x960 | 120Hz | 4:3 | reduced blanking |
| 35 | 1280x1024 | 60Hz | 5:4 | |
| 36 | 1280x1024 | 75Hz | 5:4 | |
| 37 | 1280x1024 | 85Hz | 5:4 | |
| 38 | 1280x1024 | 120Hz | 5:4 | reduced blanking |
| 39 | 1360x768 | 60Hz | 16:9 | |
| 40 | 1360x768 | 120Hz | 16:9 | reduced blanking |
| 41 | 1400x1050 | 60Hz | 4:3 | reduced blanking |
| 42 | 1400x1050 | 60Hz | 4:3 | |
| 43 | 1400x1050 | 75Hz | 4:3 | |
| 44 | 1400x1050 | 85Hz | 4:3 | |
| 45 | 1400x1050 | 120Hz | 4:3 | reduced blanking |
| 46 | 1440x900 | 60Hz | 16:10 | reduced blanking |
| 47 | 1440x900 | 60Hz | 16:10 | |
| 48 | 1440x900 | 75Hz | 16:10 | |
| 49 | 1440x900 | 85Hz | 16:10 | |
| 50 | 1440x900 | 120Hz | 16:10 | reduced blanking |
| 51 | 1600x1200 | 60Hz | 4:3 | |
| 52 | 1600x1200 | 65Hz | 4:3 | |
| 53 | 1600x1200 | 70Hz | 4:3 | |
| 54 | 1600x1200 | 75Hz | 4:3 | |
| 55 | 1600x1200 | 85Hz | 4:3 | |
| 56 | 1600x1200 | 120Hz | 4:3 | reduced blanking |
| 57 | 1680x1050 | 60Hz | 16:10 | reduced blanking |
| 58 | 1680x1050 | 60Hz | 16:10 | |
| 59 | 1680x1050 | 75Hz | 16:10 | |
| 60 | 1680x1050 | 85Hz | 16:10 | |
| 61 | 1680x1050 | 120Hz | 16:10 | reduced blanking |
| 62 | 1792x1344 | 60Hz | 4:3 | |
| 63 | 1792x1344 | 75Hz | 4:3 | |
| 64 | 1792x1344 | 120Hz | 4:3 | reduced blanking |
| 65 | 1856x1392 | 60Hz | 4:3 | |
| 66 | 1856x1392 | 75Hz | 4:3 | |
| 67 | 1856x1392 | 120Hz | 4:3 | reduced blanking |
| 68 | 1920x1200 | 60Hz | 16:10 | reduced blanking |
| 69 | 1920x1200 | 60Hz | 16:10 | |
| 70 | 1920x1200 | 75Hz | 16:10 | |
| 71 | 1920x1200 | 85Hz | 16:10 | |
| 72 | 1920x1200 | 120Hz | 16:10 | reduced blanking |
| 73 | 1920x1440 | 60Hz | 4:3 | |
| 74 | 1920x1440 | 75Hz | 4:3 | |
| 75 | 1920x1440 | 120Hz | 4:3 | reduced blanking |
| 76 | 2560x1600 | 60Hz | 16:10 | reduced blanking |
| 77 | 2560x1600 | 60Hz | 16:10 | |
| 78 | 2560x1600 | 75Hz | 16:10 | |
| 79 | 2560x1600 | 85Hz | 16:10 | |
| 80 | 2560x1600 | 120Hz | 16:10 reduced blanking |
| 81 | 1366x768 | 60Hz | 16:9 | |
| 82 | 1920x1080 | 60Hz | 16:9 | 1080p |
| 83 | 1600x900 | 60Hz | 16:9 | reduced blanking |
| 84 | 2048x1152 | 60Hz | 16:9 | reduced blanking |
| 85 | 1280x720 | 60Hz | 16:9 | 720p |
| 86 | 1366x768 | 60Hz | 16:9 | reduced blanking |
[/tab]
[/tabs]

参考链接：
[https://www.raspberrypi.org/documentation/configuration/config-txt/video.md](https://www.raspberrypi.org/documentation/configuration/config-txt/video.md)
[https://www.raspberrypi.org/documentation/configuration/config-txt/conditional.md](https://www.raspberrypi.org/documentation/configuration/config-txt/conditional.md)

[comment]: # (##{"timestamp":1594102080}##)