Luckfox-Pico-Pro-Max是一款集成`0.5TOPS NPU`的`Arm Cortex-A7`处理器`RV1106G3`的小型开发板。主频为`1.2GHz`，片载内存`256MB DDR3L`，板载`256MB SPI FLASH`，最方便的是板载网口。另外还有[瑞芯微](https://www.rock-chips.com/a/cn/news/rockchip/2022/0217/1541.html)的`RV1103`等都是片载内存的QFN芯片，适合做一些小型嵌入式机器学习的功能。

## buildroot
啥都不修改直接编译的过程可以参考下面的链接，用于验证环境搭建是否正确。
参考链接：https://github.com/LuckfoxTECH/luckfox-pico/blob/main/README_CN.md

### buildroot配置修改
```
cd sysdrv/source/buildroot/buildroot-2023.02.6/
sudo make luckfox_pico_defconfig
sudo make menuconfig
```

修改完buildroot后，保存配置并重新编译
```
sudo make savedefconfig 
sudo make
cd /opt/luckfox-pico
sudo ./build.sh
```

参考链接：https://wiki.luckfox.com/zh/Luckfox-Pico/Luckfox-Buildroot/

### kernel配置修改
```
cd sysdrv/source/kernel
sudo cp ./arch/arm/configs/luckfox_rv1106_linux_defconfig .config
sudo make ARCH=arm menuconfig
```

修改完kernel后，保存配置并重新编译
```
sudo make ARCH=arm savedefconfig
sudo cp defconfig arch/arm/configs/luckfox_rv1106_linux_defconfig
cd /opt/luckfox-pico
sudo ./build.sh kernel
```

参考链接：https://wiki.luckfox.com/zh/Luckfox-Pico/Luckfox-Pico-USB

### 报错处理

1. 使用瑞芯微工具套件 v1.85 `SocToolKit`下载固件时报错无法找到`oem.img`
```
拷贝镜像文件需要用指令，不能使用win的复制粘贴。
sudo cp -r output/image/ /mnt/d/linux/luckfox/image
```

2. fakeroot的报错，这个在[WSL子系统编译buildroot填坑](https://blog.meekdai.com/post/WSL-zi-xi-tong-bian-yi-buildroot-tian-keng.html)中有记录，但是无法解决。
```
需要修改sysdrv/tools/pc/mtd-utils/mkfs_ubi.sh文件，把两处的which fakeroot替换为which fakeroot-tcp即可。如下：

if which fakeroot-tcp; then
	FAKEROOT_TOOL="`which fakeroot-tcp`"
	echo "chown -h -R 0:0 $ROOTFS_SRC_DIR" >> $ROOTFS_IMAGE_FAKEROOT_UBI
```

## Ubuntu
目前Ubuntu编译没有特殊问题，只需要切换WSL的版本为Ubuntu-22.04。

但是需要注意的是，Ubuntu系统目前只能下载到TF卡上，并且需要擦除`SPI Flash`上的固件，因为芯片默认第一启动选项是`SPI Flash`，在`SPI Flash`上无法找到系统才会加载TF卡上的系统。

目前Ubuntu系统不支持官方的SC3336摄像头，见[Pico Max的Ubuntu系统无法检测到摄像头](https://forums.luckfox.com/viewtopic.php?t=22)

参考链接：https://wiki.luckfox.com/zh/Luckfox-Pico/Luckfox-Pico-Flash-burn-image
参考链接：https://wiki.luckfox.com/zh/Luckfox-Pico/Luckfox-Pico-SD-Card-burn-image


