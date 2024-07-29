在2023年11月14号开始生效，阿里云这是要开始割韭菜了。去年我还有篇文章写了[《网站配置SSL证书》](https://blog.meekdai.com/post/wang-zhan-pei-zhi-SSL-zheng-shu.html)的方便快捷，今天突然发现免费证书的1年手动续一次，改为了3个月续一次。

【变更】关于免费证书服务策略调整通知
https://help.aliyun.com/zh/ssl-certificate/product-overview/notice-on-adjustment-of-service-policies-for-free-certificates?spm=0.2020520163.0.0.45d3OWnYOWnYe5

关于HTTPS免费证书停止自动续签的公告
https://help.aliyun.com/zh/cdn/product-overview/terminate-automatic-renewal-of-free-ssl-certificates

从这两个通知中可以看出，之后要么寻找其他的免费证书，要么老老实实的买68一年的付费证书。目前还是等到期了再看看阿里云有没有提前邮件通知，以及续签的方便程度来决定是否需要折腾一下其他免费证书。

后续如果有推荐的免费证书或者有啥自动续签的方式，再来记录了。

### 20240729更新

突然发现解析到Github的二级域名，只需要在仓库的设置里面勾选`Enforce HTTPS`后，会自动申请[Let's Encrypt](https://letsencrypt.org/)证书，非常方便。

然后也试用了一下[certd](https://github.com/certd/certd)这个开源项目，可以直接通过docker部署，自动申请证书以及上传证书到阿里云。

不过目前也就只有 https://meekdai.com/ 这一个顶级域名需要每过3个月重新申请一下，目前来说还是很方便的，只需要2个步骤如下。

> [!TIP]
> 1. SSL证书管理页面申请新的证书
> 2. 通过后，点击部署，直接部署到对应的OSS即可


