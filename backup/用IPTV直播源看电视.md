电视家下线有一段时间了，我基本不看直播电视无所谓，但是家里长辈要看，所以一直想找个方便可靠的给家里的电视装上。今天在`github`上发现了一个非常不错的项目，下面分享一下使用的方法。


### 下载Tivimate
有能力的可以通过google商店安装正版软件，如果是测试学习一下，可以点击下载[TiviMate-2.1.5_付费破解版.apk](https://github.com/skysolf/iptv/blob/main/TiviMate%20%202.1.5%20-%20Premium%E4%BB%98%E8%B4%B9%E7%A0%B4%E8%A7%A3%E7%89%88.apk)

### 安装Tivimate
我家里是小米电视，一般如果是安卓电视应该都可以安装。

1. 有U盘还有电脑的可以直接拷贝上面下载的`apk`文件到U盘，然后把U盘插到电视上直接安装。
2. 如果是远程给别人安装，建议把apk文件上传到迅雷云盘中，然后在电视上安装迅雷云盘，通过迅雷云盘下载安装。
3. 其实还有很多种安装方式，但是目的都是把apk文件上传到电视，只要目的达到就行。

### 添加直播源
安装好`Tivimate`后，直接打开，然后往里面添加一个源地址就行。我之前说的非常不错的开源项目就是一个直播源[IPTV](https://github.com/Meroser/IPTV)。因为`github`有些时候没有科学上网的话会无法访问，所以这个开源项目里面的订阅地址用了镜像源，这导致了需要输入的地址就非常非常长，如下：
````
https://mirror.ghproxy.com/https://raw.githubusercontent.com/Meroser/IPTV/main/IPTV.m3u
````
因为在电视上输入这一段实在太~~，所以我用我的二级域名做了一个显性重定向，所以只需要添加源地址的时候输入下面这个就可以了：
```
http://iptvs.meekdai.com
```

### 其他
1. 需要注意的是，这个直播源目前是`IPV6`的，如果你的宽带不支持，或者路由器光猫还没有开启`IPV6`，则需要先解决`IPV6`的问题。
2. 后续如果有找到更好的，或者有`IPV4`的直播源，也会在本篇文章里面添加。
3. 另外我也在我的iPhone上测试了一下，下载`APTV`这个软件，然后添加上面的源，一样可以愉快的看电视。

### 参考链接：
https://github.com/Meroser/IPTV
https://github.com/skysolf/iptv
https://github.com/fanmingming/live
https://github.com/Moexin/IPTV
https://www.znds.com/tv-1236500-1-1.html
https://github.com/ssili126/tv (IPV4)
https://github.com/Ftindy/IPTV-URL
https://github.com/mlvjfchen/zby

```
目前有些IPTV仓库的作者有删库跑路的情况，所以上面的参考链接可以多去看看，有一些还是可以用的。
```




