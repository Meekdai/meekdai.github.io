[Gmeek](https://github.com/Meekdai/Gmeek) 一个博客框架，超轻量级个人博客模板，完全基于`Github Pages `、 `Github Issues` 和 `Github Actions`，可以称作`All in Github`。不需要本地部署，从搭建到写作，只需要18秒，2步搭建好博客，第3步就是写作。

### 一、安装
> 安装及其简单，但是也要认真看下面的步骤，一步一步来。
1. 【创建仓库】点击[通过模板创建仓库](https://github.com/new?template_name=Gmeek-template&template_owner=Meekdai)，建议仓库名称为`XXX.github.io`，其中`XXX`为你的github用户名。

2. 【启用Pages】在你创建好的仓库的设置`Settings`中`Pages->Build and deployment->Source`下面选择`Github Actions`。

3. 【开始写作】打开一篇issue，开始写作，并且添加一个标签（只添加一个），保存issue后会自动创建博客内容，片刻后可通过https://XXX.github.io 访问

4. 【手动全局生成】这个步骤只有在修改`config.json` 文件或者出现奇怪问题的时候，需要执行。
```P4
通过Actions->build Gmeek->Run workflow->里面的按钮全局重新生成一次
```

### 二、配置文件
> 按照安装步骤成功搭建好后，就可以阅读下面的内容修改配置文件啦。
> 注意修改配置文件后一定要手动全局生成一次，不然会报错。
> 如果对`json`格式不熟悉，建议先简单学习一下。

`config.json` 文件就是配置文件，在创建的仓库内可以找到，对应修改为自己的即可。
```javascript
{
    "title":"Meekdai",
    "subTitle":"童话是一种生活态度，仅此而已。",
    "avatarUrl":"https://github.githubassets.com/favicons/favicon.svg",
    "GMEEK_VERSION":"last"
}
```
以上是必须的字段，下面是可以自定义字段的描述，可以选择加入到`config.json`中。

```javascript
"displayTitle":"Meekdai",
"homeUrl":"http://blog.meekdai.com",
"faviconUrl":"https://github.githubassets.com/favicons/favicon.svg",
"email":"meekdai@163.com",
"startSite":"02/16/2015",
"filingNum":"浙ICP备20023628号",
"onePageListNum":15,
"singlePage":[],
"commentLabelColor":"#006b75",
"yearColorList":["#bc4c00", "#0969da", "#1f883d", "#A333D0"],
"i18n":"CN",
"UTC":8,
"dayTheme":"light",
"nightTheme":"dark_colorblind",
"urlMode":"pinyin",
"style":"",
"script":"",
```

| **配置参数**       | **说明** | 
|----------------|----------------|
| title | 【必填】博客标题 |
| subTitle | 【必填】博客描述&自述 |
| avatarUrl | 【必填】博客头像 |
| GMEEK_VERSION | 【必填】Gmeek版本，一般写`last`也可以用具体tag版本 |
| displayTitle | 用于头像后面的标题展示，如果和`title`一致则不用添加 |
| homeUrl | 博客的主页地址，自定义域名时需要配置 |
| faviconUrl | 页面的favicon地址，如果和avatarUrl一致则不用添加 |
| email | 用于自动提交仓库时用，不添加也可以 |
| startSite | 用于页面底部显示网站运行天数 |
| filingNum | 用于页面底部显示备案信息 |
| onePageListNum | 用于首页每页展示的文章数量 |
| singlePage | 自定义独立页面，例如`about`或者`link` |
| commentLabelColor | 用于自定义显示评论数量标签的颜色 |
| yearColorList | 用于自定义显示不同年份标签的颜色 |
| i18n | 用于定义博客语言，目前支持`EN`/`CN`/`RU` |
| UTC | 用于定义[时区](https://en.wikipedia.org/wiki/List_of_UTC_offsets) |
| dayTheme | 用于定义[亮主题](https://github.com/settings/appearance) |
| nightTheme | 用于定义[暗主题](https://github.com/settings/appearance) |
| urlMode | 用于定义文章链接生成模式，目前支持`pinyin`/`issue`/`ru_translit` |
| style | 用于自定义文章页全局CSS |
| script | 用于自定义文章页全局JavaScript |

### 三、常见问题
1. 搭建不成功
> 多半是没有按照安装步骤来，其实搭建就这2步，不要自己乱点乱设置，就不会有问题。
> 案例一：https://github.com/Meekdai/Gmeek/issues/14 
> 案例二：https://github.com/Meekdai/Gmeek/issues/18
> 案例二：https://github.com/Meekdai/Gmeek/issues/20

2. Actions执行失败
> 修改了config.json配置文件后，需要全局生成。另外label标签没有打，或者多打也会出现这个问题。
> 建议通过Actions->build Gmeek->Run workflow->里面的按钮全局重新生成一次
> 案例一：https://github.com/Meekdai/Gmeek/issues/1
> 案例二：https://github.com/Meekdai/Gmeek/issues/10

3. 如果要导入以前的文章，如何设置发布时间呢？ 
> 如需修改发布时间，可以在文章最后一行添加如下代码。里面的时间是采用时间戳的形式，可以用如下[网站](https://tool.lu/timestamp)转换。  
```html
<!-- ##{"timestamp":1490764800}## -->
```

4. 自定义单篇文章页面的`style`和`script`
```html
<!-- ##{"style":"<style>#postBody{font-size:20px}</style>"}## -->
```
```html
<!-- ##{"script":"<script async src='//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'></script>"}## -->
```

6. 可同时一起添加多种自定义参数：  
```html
<!-- ##{"script":"<script async src='//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'></script>","style":"<style>#postBody{font-size:20px}</style>","timestamp":1490764800}## -->
```

7. 添加全局文章页面的`style`和`script`
> 在config.json文件中添加
```javascript
"style":"<style>#postBody{font-size:20px}</style>",
"script":"<script async src='//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'></script>",
```

8. 置顶博客文章,只需要`Pin issue`即可。

9. 如果在评论里面登录后评论报错，可直接按照提示安装`utteranc app`即可
> Error: utterances is not installed on xxx/xxx.github.io. If you own this repo, install the app. Read more about this change in the PR.

### 如何魔改
如果有朋友想修改博客的主题，或者添加一些东西，这个框架是支持魔改的。所有的UI都在[templates](https://github.com/Meekdai/Gmeek/tree/main/templates)文件中，可进行修改，如果合适，我会合并到主线，通过配置文件让用户选择哪个主题。




