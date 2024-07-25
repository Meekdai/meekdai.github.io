为了使得Gmeek的功能更加的丰富，我添加了插件的功能，目前已经有几个插件可以使用。大家可以直接复制文章中的配置代码使用，也可以把对应的插件文件拷贝到自己的static文件夹下使用。

## 不蒜子
> [!TIP]
> [不蒜子](https://busuanzi.ibruce.info/)是一个极简网页计数器，很多同学都希望有这个功能，所以这个插件就来了。
> 目前更推荐使用下面的Vercount插件

1. 全站添加不蒜子，只需要在config.json文件内添加配置
```
"allHead":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekBSZ.js'></script>",
```

2. 单个文章页添加不蒜子，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekBSZ.js'></script>"}## -->
```

## Vercount
> [!TIP]
> 目前发现了不蒜子官方有一个BUG，就是Safari浏览器统计的pv数据不准确，具体可见文章[解决不蒜子 (busuanzi) 文章计数出错问题](https://jdhao.github.io/2020/10/31/busuanzi_pv_count_error/)。所以找了一个可以兼容不蒜子的计数工具 [Vercount](https://github.com/EvanNotFound/vercount)。不蒜子中的数据都会自动同步过来，非常方便。

1. 全站添加Vercount，只需要在config.json文件内添加配置
```
"allHead":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekVercount.js'></script>",
```

2. 单个文章页添加不蒜子，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekVercount.js'></script>"}## -->
```

## TOC目录

> [!TIP]
> 效果预览：[markdown测试页面](https://meekdai.github.io/post/markdown-ce-shi-ye-mian.html)
> 如果某些文章比较长，里面有很多h1、h2、h3、h4等标题，就可以在右边显示TOC目录，方便导航到对应位置。

1. 所有文章页添加TOC目录，只需要在config.json文件内添加配置
```
"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekTOC.js'></script>",
```

2. 单个文章页添加TOC目录，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekTOC.js'></script>"}## -->
```

## articletoc

> [!TIP]
> 效果预览：[Markdown语法总览](https://code.buxiantang.top/post/Markdown-yu-fa-zong-lan.html) 在右下角有个圆形按钮。
> 本插件由[Tiengming](https://code.buxiantang.top/)编写，也是一个非常不错的TOC目录插件。配置方式和上面一样，只需要替换地址为如下地址即可。

```
https://blog.meekdai.com/Gmeek/plugins/articletoc.js
```

## 灯箱插件

> [!TIP]
> 效果预览：[养鱼？我应该不行](https://blog.meekdai.com/post/yang-yu-%EF%BC%9F-wo-ying-gai-bu-xing.html) 点击图片就会出现灯箱效果。
> 本插件由[Tiengming](https://code.buxiantang.top/)编写，可以放大浏览文章中的图片，适合一些图片较多的文章。

1. 所有文章页添加lightbox，只需要在config.json文件内添加配置
```
"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/lightbox.js'></script>",
```

2. 单个文章页添加lightbox，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/lightbox.js'></script>"}## -->
```

## 多插件使用

同时在所有文章页使用`TOC目录`和`灯箱插件`，需要这样添加配置文件：
```
"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekTOC.js'></script><script src='https://blog.meekdai.com/Gmeek/plugins/lightbox.js'></script>",
```
同时在一篇文章页使用`TOC目录`和`灯箱插件`，需要这样添加配置文件：
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekTOC.js'></script><script src='https://blog.meekdai.com/Gmeek/plugins/lightbox.js'></script>"}## -->
```

> [!CAUTION]
> 需要特别注意区分`script` `head` `allHead` 等这些键的用途，详细请参考 [Gmeek快速上手](https://blog.meekdai.com/post/Gmeek-kuai-su-shang-shou.html#%E4%BA%8C%E3%80%81%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)


## 其他
有了插件就可以在基础版的Gmeek框架上玩出很多很多定制化的功能，简单的UI修改也可以通过插件实现，只需要学习一点点前端知识，另外非常欢迎大家一起完善Gmeek，开发出更多的插件。

<!-- ##{"script":"<script src='https://blog.meekdai.com/Gmeek/plugins/GmeekTOC.js'></script>"}## -->