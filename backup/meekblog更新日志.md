在2023年的暑假，之前购买阿里云3年的活动ECS主机到期了，续费价格超级贵😭，所以打算在github page上面搭建自己的博客。看了很多不同类型的，例如[Hexo](https://github.com/hexojs/hexo)、[Hugo](https://github.com/gohugoio/hugo)这些比较有名的，也了解了很多在github上的小项目，发现了[gitblog](https://github.com/yihong0618/gitblog)，这个博客是用python抓取github issues的内容然后展示在首页`readme.md`，当即就来了灵感👏，我可以自己通过Python抓取github issues的内容，生成静态页面，不仅仅包含首页，文章页面也可以生成后存储在github上，而且也可以通过github Action来自动执行Python文件，搭建好后就不需要任何的本地操作。

目前已经实现了抓取文章页面和首页的基础程序，内容展示用了[primer/css](https://primer.style/css/)，评论直接使用[utteranc.es](https://utteranc.es/)拉取issues的评论，但是目前还只是一个简单的框架 =>> [meekblog](http://meekdai.github.io)



TODO:
- [ ] 优化首页和文章页UI，这是一个持久的事情💪
- [ ] 给首页添加页面[Pagination](https://primer.style/css/components/pagination)，例如一页展示10篇文章的标题内容，或者可以使用懒加载的方式
- [ ] 给首页添加[Timeline](https://primer.style/css/components/timeline)
- [x] 添加友情链接/关于等独立页面
- [x] 解决其他人提交issues污染博客内容的情况
- [x] 添加暗亮主题切换功能，包括评论主题也同时切换
