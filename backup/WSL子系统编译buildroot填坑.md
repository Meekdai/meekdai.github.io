之前一直用Windows的子系统`WSL`用来编译`micropython`的固件，速度很快而且文件交互起来也很方便。`buildroot`体积比较大，之前一直都是在`Github`的[codespaces](https://github.com/codespaces)上编译，但是`codespaces`有存储大小限制，所以这里记录一下在`WSL`中编译`buildroot`遇到的一些坑。

### 填坑
1. 报错 build/elf/librtld.os:raise.c:(.text+0x18bf4): more undefined references to 'rtld_errno' follow
这个错误是WSL对于挂载的文件，也就是在`/mnt/`下的所有内容都不区分大小写导致的，所以需要把编译的路径放到`/opt`下即可。

```
$ getfattr -n system.wsl_case_sensitive /mnt/d
getfattr: Removing leading '/' from absolute path names
# file: mnt/d
system.wsl_case_sensitive="0"

$ getfattr -n system.wsl_case_sensitive /opt
getfattr: Removing leading '/' from absolute path names
# file: opt
system.wsl_case_sensitive="1"
```
> 参考链接1：[glibc build errors with undefined references in files under elf/ ](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/523)   
> 参考链接2：[Linker error](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/742)   

2. 报错 fakeroot
```
fakeroot, while creating message channels: Function not implemented
This may be due to a lack of SYSV IPC support.
fakeroot: error while starting the `faked' daemon.
kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
make: *** [fs/common.mk:87: /opt/buildroot/buildroot-2018.08.2/output/build/buildroot-fs/rootfs.common.tar] Error 1
```
据微软开发人员解释，目前WSL仅仅支持SYSV的信号量，消息队列还没有被实现(fakeroot需要SYSV的消息队列)。所以解决方案是使用`fakeroot-tcp`替换`fakeroot`
```
sudo apt-get install -y fakeroot
sudo cp -f /usr/bin/fakeroot-tcp output/host/usr/bin/fakeroot
```

> 参考链接1：[Sysvipc message queues and fakeroot](https://github.com/microsoft/WSL/issues/2465)   
> 参考链接2：[Win10 WSL系统下编译buildroot报错不支持SYSV IPC，导致fakeroot无法正常工作](https://whycan.com/t_1004.html)   

3. How to remove Windows paths from WSL path
```
echo $PATH
$ sudo vi /etc/wsl.conf

[interop]
appendWindowsPath = false
```
修改后重启WSL，即可删除Windows上的环境变量

### WSL指令

```
重启WSL
Restart-Service LxssManager

转换 WSL 版本2
wsl --set-version ubuntu-20.04 2

列出可用的 Linux 发行版本
wsl --list --online

列出已安装的 Linux 发行版本
wsl --list --verbose

关机
wsl --shutdown

注销或卸载 Linux 发行版
wsl --unregister <DistributionName>

安装指定 Linux 发行版
wsl --install --distribution Ubuntu-22.04

运行指定 Linux 发行版
wsl --distribution Ubuntu-22.04

```
> 参考链接1：[WSL 的基本命令](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands)   


