最近搬出了读大学的时候斥巨资买的`Macbook Pro`，当时买来差不多要1万元。刚刚在闲鱼看了一下，同款机器有人挂368元 :sob:  。这么多年过去了，其实这个台电脑刷刷网页，看看视频应该问题不大。所以打算给它折腾起来，焕发第二春。

正好有之前台式机淘汰下来的`128G`的SSD，更换掉原来的机械硬盘应该还可以快不少。本来的意图是安装双系统的，但是当我换上SSD开机后，居然直接进入`WIN10`的系统了。想着还是`WIN10`用的多，`macOS`也好多年没有用了，单系统就单系统吧。这样就变成了一台只有`WIN10`系统的`Macbook Pro`。

由于SSD里面都是台式机上的东西，安装了不少东西，开机运行的东西非常多，所以一不做二不休，直接重置系统，然后通过`windows update`更新到`WIN10 22H2`的版本。发现触控板和扬声器不能正常使用，于是网上找了一些教程，下面记录一下解决的过程。

### 触控板驱动
触控板很简单，在`github`上有大神做了开源的驱动代码，在`github上`的`Release`页面下载驱动，安装一下就可以了。具体就是解压安装包`Drivers-amd64-ReleaseMSSigned.zip`，找到`AmtPtpDevice.inf`文件，然后右键安装即可。

参考链接：[https://github.com/imbushuo/mac-precision-touchpad](https://github.com/imbushuo/mac-precision-touchpad)

### 声卡驱动
发现声卡驱动有一个打了叹号的，错误代码10。网上的教程五花八门，我也捣鼓了很久，最后通过安装`BootCamp`解决了。原文说的是安装`BootCamp6.0`，但是我用的是`BootCamp5.1`同样解决了问题。具体就是通过下面的参考链接2，下载`BootCamp5.1.5769`，解压后在`Drivers->Apple`里面找到`BootCamp.msi`，然后在此文件夹运行CMD指令，通过CMD指令运行`BootCamp.msi`文件即可。

参考链接1：[https://www.feng.com/post/10799869](https://www.feng.com/post/10799869)
参考链接2：[https://support.apple.com/kb/DL1837](https://support.apple.com/kb/DL1837)

### 键盘驱动
本来键盘驱动是正常的，但是使用了一天后发现`fn`的功能键不起作用，怀疑驱动有问题，果然用的是`HID`的通用驱动代码。这里用`BootCamp5.1.5769`里的`AppleKeyboardInstaller64.exe`安装失败，所以找了更老一点的驱动，用的`BootCamp5.1.5.1.5621`里面的驱动成功解决，可以通过`fn+F11`调节音量了。

参考链接：[https://support.apple.com/kb/DL1720](https://support.apple.com/kb/DL1720)

### 系统精简
最近又发现了`ATLASOS`这个开源项目，它可以极致精简系统，删除一些不必要的东西，让老旧电脑CPU可以流畅运行`WIN10`，所以也直接用在了我的`Macbook`中。

要通过`ATLASOS`精简系统，必须满足2个条件，第一个是系统已激活，第二个是系统已经升级到`22H2`版本。下面的链接可以找到这些工具。然后通过`ATLAS`官网下载`AME Wizard`和`Playbook`，把`Playbook`中后缀名为`.apbx`的文件拉进`AME Wizard`，然后按步骤禁用一些系统工具后就可开始自动安装`ATLAS`了。

ATLAS官网：[https://atlasos.net/](https://atlasos.net/)
AME Wizard：[https://ameliorated.io/](https://ameliorated.io/)
云萌激活工具：[https://cmwtat.cloudmoe.com/cn.html](https://cmwtat.cloudmoe.com/cn.html)
云萌开源地址：[https://github.com/TGSAN/CMWTAT_Digital_Edition](https://github.com/TGSAN/CMWTAT_Digital_Edition)
mbp技术规格：[https://support.apple.com/zh-cn/HT201300](https://support.apple.com/zh-cn/HT201300)
