Code-Server是一款网页版的IDE，相当于VSCode网页版，搭建完成后可以随时随地访问自己的代码，非常方便。但是如果没有启用HTTPS的话，有些功能就会受限制，比如命令行界面不能右键粘贴。

## 证书申请
可以直接通过阿里云等服务商申请免费的SSL证书。如果有宝塔也可以使用宝塔自带的`Let's Encrypt`申请。成功后可以得到`密钥(KEY)`和`证书(PEM格式)`两个文件。需要存放到一个合适的位置。

## 配置证书
在`coder/.config/code-server/config.yaml`中把配置`cert: false`修改如下，下面这两个文件对应上面申请的2个文件的路径，特别注意文件的权限问题。

```
cert: /home/docker/cert/xxx_public.crt
cert-key: /home/docker/cert/xxx.key
```
然后重启Code-Server服务就可以通过https来访问了。

## 其他

这里遇到一个其他问题， **浏览器自动将http跳转至https导致无法访问的问题** ，因为一个域名在浏览器中通过https访问后，之后如果访问同一个域名的不同端口的内容，如果这个端口提供的服务不支持https就会导致这个问题。

在Chrome中解决办法如下
1. 访问 chrome://net-internals/#hsts
2. Delete domain security policies 一栏里面填写这个域名点击`Delete`按钮即可
3. 这个方法是一次性的

参考链接：[centos搭建code-server及配置HTTPS、登录页自定义](https://juejin.cn/post/7230335974085525541)



