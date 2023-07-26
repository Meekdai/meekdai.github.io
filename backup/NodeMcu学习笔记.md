超简单的物联网开发平台[NodeMcu][1]，一款开源快速硬件原型平台，包括固件和开发板，用几行简单的Lua脚本就能开发物联网应用。

##NodeMCU 简介

NodeMCU 是一款开源的物联网开发平台，其固件和开发板均开源，自带 WIFI 模块。基于该平台，用几行简单的 Lua 脚本就能开发物联网应用。

其主要特点如下：

 - 像 Arduino 一样操作硬件 IO 提供硬件的高级接口，可以将应用开发者从繁复的硬件配置、寄存器操作中解放出来。用交互式 Lua 脚本，像 Arduino 一样编写硬件代码！
 - 用 Nodejs 类似语法写网络应用 事件驱动型 API 极大的方便了用户进行网络应用开发，使用类似 Nodejs 的方式编写网络代码，并运行于 5mm*5mm 大小的 MCU 之上，加快您的物联网开发进度。
 - 超低成本的 WIFI 模块 用于快速原型的开发板，集成了售价低于 10 人民币 WIFI 芯片 ESP8266，为您提供性价比最高的物联网应用开发平台。

基于乐鑫 ESP8266 的 NodeMCU 开发板，具有 GPIO、PWM、I2C、1-Wire、ADC 等功能，结合 NodeMCU 固件为您的原型开发提供最快速的途径。

NodeMCU 最新版为 1.0，如下图：

![4004543695.jpg][2]

其硬件详细配置如下：

核心模组为 ESP8266

>     MCU 为 Xtensa L106
>     RAM 50K
>     Flash 512K
>     D1~D10：10 GPIO, 每个都能配置为 PWM, I2C, 1-wire
>     FCC 认证的 WIFI 模块，内置 PCB 天线，可作为 AP

CP2102 USB 串口，即插即用（官方驱动支持 Windows, OS X，Linux 以及 VMware）

##选择开发系统 

NodeMCU 目前支持的开发主机系统类型涵盖 Windows，Linux 和 Mac OS X，也支持通过 VMware 虚拟机搭建的 Linux 环境。
我用的是Windows，并且用了[cmder][3]来优化命令行的用户体验。有关cmder的使用笔记，后面会有文章详细记录。

![1384392589.jpg][4]

##安装串口驱动

在选定开发系统后，接下来就是要安装串口驱动，打通开发主机与 NodeMCU 板子的通信，以便烧录固件、执行命令或者上传 Lua 程序。

因为 NodeMCU 1.0 采用了 cp2102 USB 串口，其驱动完美支持 Windows，Linux，OS X 和 VMWare，所以各个平台下载 [CP210x][5] 安装上即可。

对于 VMware + Linux，除了在开发主机上安装好串口驱动外，需要在插入 USB 串口以后，根据提示，允许 VMware 控制该 USB 串口，也可以通过设置/Settings 的 USB & Bluetooth 来进行设置。

在命令行下运行，看驱动是否正确加载。 

    $ ls -l /dev/tty*

下面你需要一个串口通信工具，在 Linux 下推荐 minicom

    $ sudo apt-get install minicom

在Windows下推荐SecureCRT（https://securecrt.en.softonic.com/），或者自行下载。

使用串口通信工具之前，需要明确 NodeMCU 1.0 的串口属性。NodeMCU 1.0 的启动时波特率为 74880，但是启动后就切到了 9600，如果直接用 9600，则开头会看到一串乱码之后恢复正常。而刷固件时可以通过 esptool 自己设置波特率，NodeMCU 1.0 那边会根据用户设置自动配置波特率，比如说设置成 115200，921600 都可以。

串口设备在不同系统下名字有些差异，在 Linux 下为 `/dev/ttyUSBn`，在 Mac OS X 下为 `/dev/cu.SLAB_USBtoUART` 和 `/dev/tty.SLAB_USBtoUART`，Windows 下为 `COMn`。

其他配置为常见的：`8N1`，即 Bits：8；Parity：None；Stop Bits：1。另外，Hardware Flow Control 和 Software Flow Control 均为 No 。

##下载并烧录最新固件

###在Linux下

从 [NodeMCU Firmware Release][6] 下载最新固件，以 float 为例（注：integer 不支持 float，但节省了 11 KB）：

    $ wget -c https://github.com/nodemcu/nodemcu-firmware/releases/download/0.9.6-dev_20150704/nodemcu_float_0.9.6-dev_20150704.bin

接着咱们把烧录工具 esptool.py 下载下来。同时安装其他必要工具。

    $ sudo apt-get install git python python-serial python-setuptools
    $ git clone https://github.com/themadinventor/esptool.git
    $ cd esptool
    $ python setup.py install

在烧录固件之前需要通过如下操作进入 NodeMCU 的固件烧录模式：

 - 按住 FLASH 按键（这里不松开）
 - 按下 RST 按键并松开
 - 松开 FLASH 按键

接着通过 esptool.py 烧录固件：

    $ sudo esptool.py --port /dev/ttyUSB0 write_flash -fm dio -fs 32m -ff 40m 0x00000 nodemcu_float_0.9.6-dev_20150704.bin

烧录完以后记得按下 RST 重启进入新固件。

esptool.py 烧写时默认的通信波特率为 115200，为了加速烧写速度，可以通过 --baud 921600 设置为 921600。

需要提到的是，如果不想保留固件中原有的各类 Lua 程序，可以在启动后格式化文件系统（file.format()，见后文），也可以在烧录前刷掉整个固件：

    $ sudo esptool.py --port /dev/ttyUSB0 erase_flash

当文件系统被破坏或者某个 Lua 程序出错以后导致系统不断重启时，擦除整个 Flash 几乎是必要的（实际也可以擦除文件系统所在的区块或者重写该区块），当然，还有一些另类的办法，后面会补充。

###在Windows下

固件下载地址：[NodeMCU Firmware Release][7]
一键烧录软件下载地址：[nodemcu-flasher][8]

打开一键烧录软件，设置固件所在目录

![2682123040.jpg][9]

设置ESP8266 FLASH信息，波特率可以自己设定，9600应该会有点慢。

![1498565922.jpg][10]

选择串口，开始烧录，有些文档说需要GPIO0拉低后上电，但是我不需要拉低也可以烧写。

![2891132200.jpg][11]

烧录完成

![1930085769.jpg][12]

上电后ESP8266从FLASH正常启动。串口波特率设置为9600，就可以和nodemcu交互了，但是复位后前面会有一段乱码有待解决。

![424483076.jpg][13]

另外，最新的NodeMCU 版本貌似没有bin文件下载，需要自己编译，这个后面再来解决。

##基本操作演示

烧录完以后按下 RST 按钮重启 NodeMCU，再启动串口工具就可以进入 Lua 交互式命令行：
在在Linux下可以用`$ minicom -D /dev/ttyUSB0`来打开串口工具，Windows下直接运行相应的软件就行了。

    > print('Hello, Meekdai')
    Hello, Meekdai
    > gpio.mode(0, gpio.OUTPUT)
    > gpio.write(0, gpio.LOW)
    > gpio.write(0, gpio.HIGH)
    > file.format()
    > node.restart()

上面几条命令分别完成：

 - 打印了一串字符串
 - 开/关了靠近 USB 口的 LED（靠近 Wifi 模块的 LED 的 pin 为 4）
 - 格式化文件系统
 - 最后重启了 NodeMCU

如果嫌不够酷，可以参考 [NodeMCU API 手册][14] 可以做更多有趣的操作。

接下来，创建一个初始化程序：`init.lua`，它在 NodeMCU 启动后自动执行。

咱们通过该程序在 NodeMCU 启动后立即点亮 LED：

    > file.open('init.lua','w')
    > file.writeline('gpio.mode(0,gpio.OUTPUT)')
    > file.writeline('gpio.write(0,gpio.LOW)')
    > file.close()
    > node.restart()

`init.lua` 是 NodeMCU 启动时默认执行的第一个程序，有点类似 Linux 上的 init 程序。通过它还可以加载其他程序来完成特定的功能。

咱们再做一个复杂一点的操作，在 `init.lua` 里头调用（dofile）一个 `user.lua` 来点亮 LED：

    > file.open('init.lua','w')
    > file.writeline('dofile("user.lua")')
    > file.close()
    > file.open('user.lua','w')
    > file.writeline('gpio.mode(0,gpio.OUTPUT)')
    > file.writeline('gpio.write(0,gpio.LOW)')
    > file.close()
    > node.restart()

读出 `init.lua` 看下效果：

    > file.open('init.lua','r')
    > print(file.readline())
    dofile("user.lua")
    > file.close()

当 `user.lua` 脚本出错时可能导致系统不停地重启，这个时候除了擦除整个 Flash 外，还可以通过 `init.lua` 做个简单的容错处理：

    if gpio.read(2) == 1:
        file.format()
    else
        dofile('user.lua')
    end

一旦系统出错，只要拉高 GPIO 2 就可以格式化文件系统。

暂时先到这里吧，后面会逐步介绍更多实例。


##上传 Lua 程序

上面演示的是命令行操作，这里再介绍如何把在主机端写好的 Lua 程序上传到 NodeMCU 上。

测试过两个工具都可以用来上传 Lua 程序，分别是：

 - [luatool.py][15]：可用于命令行传送 Lua 脚本，无须复杂的图形化工具支持，同时支持通过串口和 Telnet 上传
 - [nodemcu.py][16]：除了不支持通过 Telnet 上传外，基本功能同 luatool，只是操作方式稍有差异

下载上述工具：

    $ git clone https://github.com/4refr0nt/luatool.git
    $ git clone https://github.com/md5crypt/nodemcu.py.git

两个都可以进行文件传输，第二个还可以作为串口终端，两个都依赖 pySerial，第二个还需要安装 clipboard：

    $ easy_install clipboard

在上传前咱们写一个简单的 `init.lua` 脚本，该脚本用于点亮另外一个 LED：

    print('Hello, Meekdai')
    print('I am Nodemcu')
    gpio.mode(4, gpio.OUTPUT)
    gpio.write(4, gpio.LOW)

###luatool.py

在Linux下通过 luatool.py 传送，传送完立马重启：

    $ cd luatool/luatool/
    $ sudo ./luatool.py -p /dev/ttyUSB0 -b 9600 -f init.lua -r

查看帮助，可以看到更多用法：

    $ sudo ./luatool.py -h
    Usage: luatool.py [-h] [-p PORT] [-b BAUD] [-f SRC] [-t DEST] [-c] [-r] [-d]
                      [-v] [-a] [-l] [-w] [-i] [--delete DELETE] [--ip IP]
    ESP8266 Lua script uploader.
    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  Device name, default /dev/ttyUSB0
      -b BAUD, --baud BAUD  Baudrate, default 9600
      -f SRC, --src SRC     Source file on computer, default main.lua
      -t DEST, --dest DEST  Destination file on MCU, default to source file name
      -c, --compile         Compile lua to lc after upload
      -r, --restart         Restart MCU after upload
      -d, --dofile          Run the Lua script after upload
      -v, --verbose         Show progress messages.
      -a, --append          Append source file to destination file.
      -l, --list            List files on device
      -w, --wipe            Delete all lua/lc files on device.
      -i, --id              Query the modules chip id.
      --delete DELETE       Delete a lua/lc file from device.
      --ip IP               Connect to a telnet server on the device (--ip
                            IP[:port])

在Windows下的指令如下，当然你需要先安装Python

    python ./luatool.py --port COM3 --src init.lua -r

###nodemcu.py

通过 `nodemcu.py` 上传：

    $ cd nodemcu.py/
    $ python ./nodemcu.py /dev/ttyUSB0 9600
    > :file init.lua init.lua
    > node.restart()

查看帮助，更多用法：

    > :help
    :help
    :uart [boudrate]          - dynamic boudrate change
    :load src                 - evaluate file content
    :file dst src             - write local file src to dst
    :paste [file]             - evaluate clipboard content
                                or write it to file if given
    :cross-compile dst [file] - compile file or clipboard using
                                luac-cross and save to dst
    :execute [file]           - cross-compile and execute clipboard or
                                file content without saving to flash
    :soft-compile dst [file]  - compile file or clipboard on device
                                and save do dst. This call should handle
                                lager files than file.compile

##Lua 程序示例

这里仅仅展示几则基本的 Lua 程序，方便大家快速上手。更多例子请参考 NodeMCU Firmware 下的 [lua_examples][17]

###启动后不断闪烁 LED

上面其实已经演示了 LED 的基本操作，这里再介绍一个 timer module 的 API：tmr.alarm()：

> tmr.alarm(id, interval, repeat, function do())
> 
> id: 0~6, alarmer id. Interval: alarm time, unit: millisecond repeat: 0
> - one time alarm, 1 - repeat function do(): callback function for alarm timed out

咱们基于它实现一个 `blink.lua`:

    print('Blink Demo')
    lighton=0
    led=0
    gpio.write(led, gpio.HIGH)
    tmr.alarm(0,1000,1,function()
    if lighton==0 then
        lighton=1
        gpio.mode(led, gpio.OUTPUT)
        gpio.write(led, gpio.LOW)
    else
        lighton=0
        gpio.write(led, gpio.HIGH)
    end
    end)
    gpio.mode(led, gpio.INPUT)


上传 `blink.lua` 并立即执行：

    python ./luatool.py --port COM3 --src blink.lua -r

> 这里提醒一下，在用串口下载程序的时候，需要先把串口通信工具给关闭，不然会报错

###远程控制 LED 闪烁

对于物联网来讲，远程控制很关键。咱们这里演示如何通过 Wifi 开启一个服务端口 8888 用于控制 LED，`remote_led.lua`：

    -- 开启 Wifi 并获得 NodeMCU IP 地址
    -- ssid 和 pwd 分别为自家路由器的 SSID 和访问密码
    local ssid="SSID"
    local pwd="password"
    ip=wifi.sta.getip()
    print(ip)
    if not ip then
        wifi.setmode(wifi.STATION)
        wifi.sta.config(ssid,pwd)
        print(wifi.sta.getip())
    end
    -- 开启一个 8888 的端口
    -- 并通过 node.input() 调用 Lua 解释器控制 LED
    srv=net.createServer(net.TCP)
    srv:listen(8888,function(conn)
        conn:on("receive",function(conn,payload)
        node.input("gpio.mode(0, gpio.OUTPUT)")
        node.input("gpio.write(0, gpio.LOW)")
        end)
    end)

上传 Lua 程序到服务器执行：

    python ./luatool.py --port COM3 --src remote_led.lua -r

查看 NodeMCU 获取的 IP 地址：

    > print(wifi.sta.getip())
    192.168.0.128   255.255.255.0   192.168.0.1

并测试（在Linux下）：

    $ sudo apt-get install lynx
    $ lynx 192.168.0.104:8888

###远程控制 LED 开关

创建一个`wifi_led.lua`，注意修改无线网的名称和密码。

    wifi.setmode(wifi.STATION)  
    wifi.sta.config("YOUR_NETWORK_NAME","YOUR_NETWORK_PASSWORD")  
    print(wifi.sta.getip())  
    led1 = 0  
    gpio.mode(led1, gpio.OUTPUT)  
    srv=net.createServer(net.TCP)  
    srv:listen(80,function(conn)  
        conn:on("receive", function(client,request)  
            local buf = "";  
            local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");  
            if(method == nil)then  
                _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");  
            end  
            local _GET = {}  
            if (vars ~= nil)then  
                for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do  
                    _GET[k] = v  
                end  
            end  
            buf = buf.."<h1> Meekdai LED Web Server</h1>";  
            buf = buf.."<p>GPIO0 <a href=\"?pin=ON1\"><button>ON</button></a> <a href=\"?pin=OFF1\"><button>OFF</button></a></p>";  
            local _on,_off = "",""  
            if(_GET.pin == "ON1")then  
                  gpio.write(led1, gpio.LOW);  
            elseif(_GET.pin == "OFF1")then  
                  gpio.write(led1, gpio.HIGH);   
            end  
            client:send(buf);  
            client:close();  
            collectgarbage();  
        end)  
    end)

查看 NodeMCU 获取的 IP 地址：

    > print(wifi.sta.getip())
    192.168.0.128   255.255.255.0   192.168.0.1

然后在浏览器中输入192.168.0.128，可以看到如下界面，点击ON为打开LED灯，点击OFF为关闭。

![3634745125.jpg][18]


###开启一个 Telnet 服务

先从 NodeMCU.com 下载该例子，`telnet.lua`：

    -- a simple telnet server
    s=net.createServer(net.TCP,180)
    s:listen(2323,function(c)
        function s_output(str)
          if(c~=nil)
            then c:send(str)
          end
        end
        node.output(s_output, 0)
        -- re-direct output to function s_ouput.
        c:on("receive",function(c,l)
          node.input(l)
          --like pcall(loadstring(l)), support multiple separate lines
        end)
        c:on("disconnection",function(c)
          node.output(nil)
          --unregist redirect output function, output goes to serial
        end)
        print("Welcome to NodeMCU world.")
    end)

上传并执行：

    python ./luatool.py --port COM3 --src telnet.lua -r

通过 telnet 连接：

**在Linux下：**

    $ sudo apt-get install telnet
    $ telnet 192.168.0.104 2323
    Trying 192.168.0.104...
    Connected to 192.168.0.104.
    Escape character is '^]'.
    Welcome to NodeMCU world.
    > print('Hello, NodeMCU Telnet')
    Hello, NodeMCU Telnet

**在Windows下：**

需要先去启动或者关闭Windows功能中打开telnet服务，然后：

    > print(wifi.sta.getip())
    192.168.0.128   255.255.255.0   192.168.0.1
    > telnet 192.168.0.128 2323
    Welcome to NodeMcu world.

有了 telnet 服务，咱就可以不依赖串口而是直接通过 Wifi 上传 Lua 脚本了：

在Linux下：

    $ cat test.lua
    print('Upload via telnet service')
    $ sudo ./luatool.py --ip 192.168.0.104:2323 -f test.lua -d -v

在Windows下：

    $ cat test.lua
    print('Upload via telnet service')
    $ python ./luatool.py --ip 192.168.0.128:2323 -f test.lua -d -v

好了，基础的学习就到这里，我其实是一遍搜索资料，自己一遍尝试，然后记录下来的，如果后续发现什么地方不对，会对上面的内容进行修改。

  [1]: http://nodemcu.com/index_cn.html
  [2]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/b4c8e6c7-0be7-4488-8517-3034592ad1ba
  [3]: http://cmder.net/
  [4]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/73a4b628-c0f3-49a9-8fea-baa57e855dff
  [5]: http://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx
  [6]: https://github.com/nodemcu/nodemcu-firmware/releases/
  [7]: https://github.com/nodemcu/nodemcu-firmware/releases/
  [8]: https://github.com/nodemcu/nodemcu-flasher
  [9]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/144b7448-49ed-4a51-9324-9591f2228cdf
  [10]: https://github.com/Meekdai/meekdai.github.io
  [11]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/47b2cd88-787f-471b-8247-9450d334b047
  [12]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/f56ae279-c339-4ca6-a0f3-18dc0f05390d
  [13]: https://github.com/Meekdai/meekdai.github.io/assets/11755104/4ee9e4dd-c028-4e56-a9a2-ec6d1a79a327
  [14]: http://nodemcu.github.io/
  [15]: https://github.com/4refr0nt/luatool
  [16]: https://github.com/md5crypt/nodemcu.py
  [17]: https://github.com/nodemcu/nodemcu-firmware/tree/master/lua_examples
  [18]: http://meekdai.com/img/7f3b1e89gy1fzpqyc0xukj20nw0gqjst.jpg

[comment]: # (##{"timestamp":1480750440}##)