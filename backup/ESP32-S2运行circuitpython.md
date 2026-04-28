ESP32-S2是乐鑫科技最新出的一款芯片，ESP32-S2 集成了丰富的外围设备，有 43 个可编程 GPIO，可以灵活配置为 USB OTG、LCD 接口、摄像头接口、SPI、I2S、UART、ADC、DAC 等常用功能。ESP32-S2 具有 LCD 接口和 14 个可配置的电容触摸 GPIO，可为基于触摸屏和触摸板的设备提供良好的 HMI 解决方案。

之前因为ESP32芯片没有USB功能，所以在使用`micropython`的时候无法通过U盘的模式进行代码载入，而必须使用USB转串口。所以在ESP32-S2上，应该可以集成USB功能进行调试和下载。

在了解到micropython官方目前并没有计划加入ESP32-S2芯片，但是circuitpython社区在全力开发兼容。于是我在乐鑫的官方淘宝店购买了一块ESP32-S2-Saola-1R的开发板，板上搭载了ESP32-S2-WROVER模组，集成了`4Mb SPIFLASH` 以及 `2Mb SPIRAM`。

下面介绍一下载入`circuitpython`固件的步骤：

1、在[circuitpython官网][1]下载`espressif_saola_1_wrover`的固件。
2、目前esptool的正式版并没有支持ESP32-S2芯片，只有在esptool.py 3.0-dev的开发版本上有，所以需要在github上下载最新的[esptool][2]。

也可以通过git克隆：

```
git clone https://github.com/espressif/esptool.git

```

然后通过pip安装
```
pip install -e esptool
```

3、使用USB线连接电脑和开发板上的USB接口，注意这个USB接口是USB转串口。
4、通过下面的指令进行载入`circuitpython`固件，其中的`COM10`需要修改为设备管理器显示的USB转串口的端口号。

```
esptool.py --chip auto --port COM10 -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 40m --flash_size 4MB 0x0000 adafruit-circuitpython-espressif_saola_1_wrover-en_US-6.0.0-alpha.1.bin
```
5、固件下载完成后，需要找到`IO19`和`IO20`这两个管脚。`IO19`对应`USB_D-`，`IO20`对应`USB_D+`，通过自制线缆连接到电脑USB端就可以识别出ESP32-S2了，电脑会弹出一个U盘叫`CIRCUITPY`的盘符，可用空间是1.97MB。打开串口工具就可以连接上circuitpython了，我上面显示的信息是这样的：

```python
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
Adafruit CircuitPython 6.0.0-alpha.1 on 2020-07-03; Saola 1 w/Wrover with ESP32S2
```

最后就可以在上面正常的写入代码了，是不是比之前ESP32编写代码以及下载代码要方便很多呢？


  [1]: https://circuitpython.org/board/espressif_saola_1_wrover/
  [2]: https://github.com/espressif/esptool

[comment]: # (##{"timestamp":1595649420}##)