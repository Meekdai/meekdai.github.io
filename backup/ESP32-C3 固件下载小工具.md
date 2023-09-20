ESP32-C3内置了USB，可以使用USB进行下载，但是每次通过命令行敲指令进行下载不是很方便，所以写了几句`bat`代码，方便下载和擦除芯片。

### esp32-c3-download.bat

```bat
@echo off
echo ============================================
wmic path win32_pnpentity get caption /format:table| find "COM" 
echo ============================================
set /p COM_NUM=input COM number:
esptool.py --chip esp32c3 --port COM%COM_NUM% --baud 460800 write_flash -z 0x0 firmware.bin
pause
```

### esp32-c3-erase_flash.bat

```bat
@echo off
echo ============================================
wmic path win32_pnpentity get caption /format:table| find "COM" 
echo ============================================
set /p COM_NUM=input COM number:
esptool.py --chip esp32c3 --port COM%COM_NUM% erase_flash
pause
```

### 前置条件：
- 需要安装`esptool.py`
- 需要把固件重命名为`firmware.bin`然后放在和`bat`文件的相同目录下。

双击运行`bat`文件后，会自动列出当前的所有`COM`口，然后输入对应ESP32-C3的`COM`口号即可，不用再打开资源管理器来查看，非常的方便。

