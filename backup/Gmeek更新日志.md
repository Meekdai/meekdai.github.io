在2023年的暑假，之前购买阿里云3年的活动ECS主机到期了，续费价格超级贵😭，所以打算在github page上面搭建自己的博客。看了很多不同类型的，例如[Hexo](https://github.com/hexojs/hexo)、[Hugo](https://github.com/gohugoio/hugo)这些比较有名的，也了解了很多在github上的小项目，发现了[gitblog](https://github.com/yihong0618/gitblog)，这个博客是用python抓取github issues的内容然后展示在首页`readme.md`，当即就来了灵感👏，我可以自己通过Python抓取github issues的内容，生成静态页面，不仅仅包含首页，文章页面也可以生成后存储在github上，而且也可以通过github Action来自动执行Python文件，搭建好后就不需要任何的本地操作。

目前已经实现了抓取文章页面和首页的基础程序，内容展示用了[primer/css](https://primer.style/css/)，评论直接使用[utteranc.es](https://utteranc.es/)拉取issues的评论，但是目前还只是一个简单的框架 =>> [meekblog](http://meekdai.github.io)

#### 20230726
- 使用`if: github.event.repository.owner.id == github.event.sender.id` 辨别他人提交issues
- 修复会抓取其他用户提交的issue的BUG
- 添加底部copyright和网站运行时长
- 添加首页文章列表前的Icon图标
- 添加首页显示文章对应的`labels`，自动抓取对应github上的标签颜色

#### 20230725
- 统一首页和博客页等样式排布

#### 20230711
- 添加友情链接和关于等独立页面
- 可以手动切换暗亮主题

