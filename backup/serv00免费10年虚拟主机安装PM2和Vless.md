这几天在论坛里面看到一个免费10年的虚拟主机[serv00](https://www.serv00.com/)。简单注册了一下就可以使用了，账号和密码会直接发到注册的邮箱里，我这里使用了Gmail的邮箱。下面就是记录一下自己搭建的东西。

### 配置
1. 【开启权限】第一步需要做的就是开启可以运行自己应用的权限。`Additional services -> Run your own applications -> Enabled` 如果不开启这一项，自己的用户目录下的所有文件都无法添加可执行权限。
2. 【进入SSH】通过注册邮箱里收到的信息，用`MobaXterm`登录，就可以看到下面的信息。
```
  ____                   ___   ___
 / ___|  ___ _ ____   __/ _ \ / _ \  ___ ___  _ __ ___
 \___ \ / _ \ '__\ \ / / | | | | | |/ __/ _ \| '_ ` _ \
  ___) |  __/ |   \ V /| |_| | |_| | (_| (_) | | | | | |
 |____/ \___|_|    \_/  \___/ \___(_)___\___/|_| |_| |_|
  Revolutionary Free Hosting

 =[ Basic account info ]=
         Username: Meekdai
             Plan: FREE
  Expiration date: 2034-03-13 02:18:41
```

### 安装PM2
[PM2](https://pm2.io/) 是一款非常优秀的`node.js`进程管理工具。可以通过SSH用下面的指令一键安装。
```
bash <(curl -s https://raw.githubusercontent.com/k0baya/alist_repl/main/serv00/install-pm2.sh)
```
使用`pm2`，请直接用路径调用：`~/.npm-global/bin/pm2`，例如`~/.npm-global/bin/pm2 list` 就可以看到自己添加的应用。

另外，在`SSH`中通过下面的指令就可以开启页面监控功能。
```
~/.npm-global/bin/pm2 monitor
```
如果没有账号可以按照提示创建就可以，然后会给出登录页面的`URL`，用浏览器登录就可以看到了，非常的方便。


### 安装Vless
Vless是一个代理节点应用，可以通过SSH用下面的指令一键安装。
```
cd ~/domains && git clone https://github.com/qwer-search/serv00-vless && mv -f serv00-vless vless && cd vless && rm -f README.md
```
在serv00的管理页面上开启一个端口，`Port reservation -> Add port`添加一个`TCP`的端口号。再在`File Manager` 里面找到`Vless`的文件下的`app.js`文件，修改里面的端口号为刚刚添加的端口号。类似下面修改为了`12345`
```
const port = process.env.PORT || 12345;
```
安装依赖
```
npm install

```
安装完毕后，使用`PM2`启动并守护vless进程：
```
~/.npm-global/bin/pm2 start app.js --name vless
```
接着去你的代理客户端软件中手动添加vless配置即可：
| **Key**         | **Value**                                     |
|-----------------|-----------------------------------------------|
| **地址**        | Panel 中 WWW Websites 选项卡里的你的 Domain name |
| **端口**        | 你放行的端口                                    |
| **用户 ID**     | 37a0bd7c-8b9f-4693-8916-bd1e2da0a817           |
| **传输协议**    | ws                                            |
| **伪装域名**    | 同地址                                         |
| **ws path**     | /                                             |

上表没有给出的可以不填。

我用的客户端是[v2rayA](https://v2raya.org/docs/prologue/quick-start/)，按照这个配置就行。目前测试下来连接不是很稳定，延迟比较高，有`1000ms`以上。

### 自动化
听说`serv00`会不定时重启机器，所以我们把`PM2`添加开机自启。而且`serv00`每三个月内必须要有一次登录面板或者`SSH`连接，不然会删号，也可以通过一个脚本解决问题，接下来我会详细说明。

####【自动续期】
新建 auto-renew.sh 脚本：
```
cat > auto-renew.sh << EOF
#!/bin/bash

while true; do
  sshpass -p '密码' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -tt 用户名@地址 "exit" &
  sleep 259200  #30天为259200秒
done
EOF
```
我是新建了一个`opt`目录，在`opt`目录下创建这个脚本。另外记得把其中的密码、用户名、ssh的地址修改为你自己的。

给 `auto-renew.sh`添加可执行权限：
```
chmod +x auto-renew.sh
```
使用PM2启动：
```
~/.npm-global/bin/pm2 start ./auto-renew.sh
```
这样就会每隔一个月自动执行一次`SSH`连接，自己`SSH`自己进行续期。

####【自动启动】

在serv00的管理页面上找到`Cron jobs`选项卡，使用`Add cron job`功能添加任务，`Specify time`选择`After reboot`，即为重启后运行。`Form type`选择`Advanced`，`Command`写：
```
/home/你的用户名/.npm-global/bin/pm2 resurrect
```
添加完之后，在`SSH`窗口保存`PM2`的当前任务列表快照：
```
~/.npm-global/bin/pm2 save
```
这样每次`serv00`不定时重启任务时，都能自动调用`PM2`读取保存的任务列表快照，恢复任务列表。如果在保存了任务列表快照后又改变了任务`PM2`的任务列表，需要重新执行`pm2 save`以更新任务列表。





参考链接：https://docs.serv00.com/
参考链接：https://blog.rappit.site/2024/01/27/serv00_logs/


