当 `V3S` 以 `SPI FLASH` 作为存储空间的时候，要调试代码只有串口不是很方便，可以使用 `tftp` 进行传输，但是总感觉不是特别优雅和直观，所以下面记录一下启用 `openssh` 的过程。

### 开启

因为使用buildroot进行构建，所以直接通过 `make menuconfig` 来启用。
```
Target packages  ---> Networking applications  ---> openssh
```
之后编译下载固件。

### 配置

在配置文件中修改如下
```
vi /etc/ssh/sshd_config

# 允许root用户登录
PermitRootLogin yes

# 允许空密码登录
PermitEmptyPasswords yes
```

这样还不能启动 `openssh` ，实践中出现了很多奇奇怪怪是错误。

1. 报错 sshd: Privilege separation user sshd does not exist  
```
vi /etc/passwd
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
```

2. 报错 /var/empty must be owned by root and not group or world-writable.  
```
chown -R root.root /var/empty/ & chmod 744 /var/empty/
```

3. 报错 WARNING: Your password has expired.
```
date -s 1801090852
passwd root
```

### 运行

```
/usr/sbin/sshd
ps | grep sshd
```

然后打开 `MobaXterm` ，选择SSH连接，添加对应的用户名和密码，就成功连接了。

![image](https://github.com/Meekdai/meekdai.github.io/assets/11755104/44bc625a-d297-42f1-8bef-815227aee492)

左边可以进行文件的上传和下载操作，也可以修改对应文件的权限等，非常方便。下面显示CPU已经RAM的使用率还有网速等，也很直观。



