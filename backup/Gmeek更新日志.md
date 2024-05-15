[Gmeek](https://github.com/Meekdai/Gmeek) 一个博客框架，超轻量级个人博客模板，完全基于`Github Pages `、 `Github Issues` 和 `Github Actions`，可以称作`All in Github`。不需要本地部署，从搭建到写作，只需要18秒，2步搭建好博客，第3步就是写作。

#### 20240515（v2.17）
- 添加Open Graph协议内容，让分享博客链接有预览
- 修复仓库名称大小写敏感的BUG
- 修复 width 拼写错误 https://github.com/Meekdai/Gmeek/issues/66

#### 20240407（v2.16）
- 修复MathJax行内公式括号误判的BUG https://github.com/Meekdai/Gmeek/issues/59
- 修复readme显示文章数量不对的BUG
- Tag页面标签显示文章数量，并且以多到少排列
- 修复页面右上角圆形按钮超出边界还能点击的BUG
- 通过exlink自定义外部链接按钮 https://github.com/Meekdai/Gmeek/issues/64
- 调整多label标签间距

#### 20240402（v2.15）
- 修复MathJax行内公式显示不正常的BUG https://github.com/Meekdai/Gmeek/issues/51
- 修复由于修改文章标题导致旧文章依旧存在的BUG https://github.com/Meekdai/Gmeek/issues/49
- 标题带有不合法符号修复 https://github.com/Meekdai/Gmeek/issues/39
- 采用rssSplit用来自定义截取RSS输出 https://github.com/Meekdai/Gmeek/issues/52
- 通过themeMode配置主题模式，默认新增跟随系统
- 添加多label支持 https://github.com/Meekdai/Gmeek/issues/56 https://github.com/Meekdai/Gmeek/issues/22

#### 20240326（v2.14）
- 修复全局`script`配置会在文章页出现2次的BUG https://github.com/Meekdai/Gmeek/issues/46
- 删除冗余`icon`地址，添加自定义`icon`功能 https://github.com/Meekdai/Gmeek/issues/40
- 修改CDN地址为[staticfile.net](https://staticfile.net/)

#### 20240314（v2.13）
- README.md文件添加统计信息以及生成时间等
- 修复时区不同导致的日期显示错误问题

#### 20240313（v2.12）
- 优化markdown2html函数
- 必填配置参数优化到4个，入门更简单
- 展示README.md文件，添加博客主页地址，方便快速进入。

#### 20240308（v2.11）
- 修复singeListJson文章的RSS地址错误的BUG
- 优化首页的用户头像图片的展示比例 https://github.com/Meekdai/Gmeek/pull/32
- Russian language support https://github.com/Meekdai/Gmeek/pull/38
- 修复tag页面title显示错误的bug
- 加载tag页面时，添加loading动画

#### 20240129（v2.10）
- 添加`mathjax`数学公式支持
- 更新RSS文件生成策略
- 通过`bottomText`可配置文章底部信息，例如`转载请注明出处`
- 通过`showPostSource`来配置是否显示github源链接 https://github.com/Meekdai/Gmeek/issues/30
- 迁移node16到20版本，原因是node16已达到其[生命周期的终点](https://github.com/nodejs/Release/#end-of-life-releases)，需要手动修改`Gmeek.yml`文件。

#### 20231216（v2.9）
- 修复创建仓库不是`XXX.github.io`导致的BUG https://github.com/Meekdai/Gmeek/pull/11
- 修复取消置顶后文章依旧置顶的BUG
- 修复CLS布局偏移问题
- 解决只有标题没有文章内容抓取失败的BUG
- 添加全局文章页`script`和`style`
- 部分SEO优化

#### 20231122（v2.7）
- 添加`Tag`标签归档功能  
- 移除临时的Google搜索框，添加页内搜索功能，速度一级棒  
- `markdown`渲染使用`gfm`格式以支持所有`github`特性  https://github.com/Meekdai/Gmeek/pull/9
- 优化手机端排列显示

#### 20231113（v2.6）
- 再一次简化搭建流程，真18秒搭建完成
- 通过urlMode配置文章URL模式

#### 20231102（v2.5）
- 修复h2 h3 h4 标签颜色变化
- 修复单页面runOne报错的BUG
- 如果存在备案号，添加链接到工信部备案官网

#### 20230905（v2.4）
- 没有代码高亮需求的文章不加载高亮CSS
- 添加`nightTheme`和`dayTheme`配置，可定义值同github的主题
- `config.json`配置文件精简

#### 20230829（v2.3）
- 修复黑色主题下刷新页面有短时白闪的BUG

#### 20230822（v2.2）
- 首页添加翻页功能，每页展示数量由`onePageListNum`配置决定
- 切换[primer/css](https://cdn.staticfile.org/Primer/21.0.7/primer.css)文件CDN为七牛云staticfile

#### 20230814（v2.1）
- 添加自定义文章页`style`和`script`
- 使用a标签优化圆形按钮
- 修改切换主题亮暗颜色，更加直观
- 不再使用`jsdelivr`，精简文件，提升页面加载速度

#### 20230812（v2.0）
- 使用jinja2重构生成html的所有代码
- 通过模板的方式后续可提供不同UI主题
- 对SEO进行优化

#### 20230804（v1.3）
- 添加文章置顶功能  :top: 
- 可自定义单篇文章的字体大小

#### 20230801（v1.2） :clinking_glasses: 
- 添加RSS
- 独立JS文件，使用jsdelivr CDN
- 添加控制台console版本号输出
- 把所有配置都统一到了`config.json`文件中，其他地方无需再修改

#### 20230731（v1.1） :poultry_leg: 
- 无需自己创建繁琐的secrets，简单3步搭建好，有手就行
- 搜索框目前指定到Google搜索
- 评论按钮加载优化，添加loading
- 支持github Emoji表情 :sparkles: 

#### 20230730
- 文章生成和部署流程合并到一个工作流中
- 添加简易的i18n，目前支持中文`CN`和英文`EN`，可以在配置文件中配置 :wink: 

#### 20230729
- 简化搭建流程，无需克隆，只需要创建自己的仓库3步轻松搭建 :smile: 

#### 20230728
- 博客框架更名为Gmeek，源码上传Github
- 修改python传递参数为Json格式
- 在列表页和文章页展示评论非0的数量（非动态）
- 评论添加按钮，点击后才加载utteranc
- 修改评论框背景色随主题
- 添加`config.json`文件，方便用户配置自己的信息

#### 20230726
- 使用`if: github.event.repository.owner.id == github.event.sender.id` 辨别他人提交issues
- 修复会抓取其他用户提交的issue的BUG
- 添加底部copyright和网站运行时长
- 添加首页文章列表前的Icon图标
- 添加首页显示文章对应的`labels`，自动抓取对应github上的标签颜色

#### 20230725
- 统一首页和博客页等样式排布

#### 20230711
- 添加友情链接和关于等独立页面 :new: 
- 可以手动切换暗亮主题

---

在2023年的暑假，之前购买阿里云3年的活动ECS主机到期了，续费价格超级贵，所以打算在github page上面搭建自己的博客。看了很多不同类型的，例如[Hexo](https://github.com/hexojs/hexo)、[Hugo](https://github.com/gohugoio/hugo)这些比较有名的，也了解了很多在github上的小项目，发现了[gitblog](https://github.com/yihong0618/gitblog)，这个博客是用python抓取github issues的内容然后展示在首页`readme.md`，当即就来了灵感，我可以自己通过Python抓取github issues的内容，生成静态页面，不仅仅包含首页，文章页面也可以生成后存储在github上，而且也可以通过 github Action 来自动执行 Python 文件，完全不需要任何的本地部署和操作。

目前已经实现了抓取文章页面和首页的基础程序，内容展示用了[primer/css](https://primer.style/css/)，评论直接使用[utteranc.es](https://utteranc.es/)拉取issues的评论，但是目前还只是一个简单的框架 =>> [Gmeek](https://github.com/Meekdai/Gmeek)

---

TODO:
- [x] 数学公式目前不支持，考虑是否添加
- [ ] 准备写第二个UI主题
- [ ] 优化CSS体积，提升加载速度