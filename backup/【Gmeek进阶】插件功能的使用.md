为了使得Gmeek的功能更加的丰富，我添加了插件的功能，目前已经有2个插件可以使用。

## 不蒜子
[不蒜子](https://busuanzi.ibruce.info/)是一个极简网页计数器，很多同学都希望有这个功能，所以这个插件就来了。

1. 全站添加不蒜子，只需要在config.json文件内添加配置
```
"allHead":"<script src='https://blog.meekdai.com/assets/GmeekBSZ.js'></script>",
```

2. 单个文章页添加不蒜子，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/assets/GmeekBSZ.js'></script>"}## -->
```

目前发现了不蒜子官方有一个BUG，就是Safari浏览器统计的pv数据不准确，具体可见文章[解决不蒜子 (busuanzi) 文章计数出错问题](https://jdhao.github.io/2020/10/31/busuanzi_pv_count_error/)。所以找了一个可以兼容不蒜子的计数工具 [Vercount](https://github.com/EvanNotFound/vercount)。只需要修改上面的配置中的`GmeekBSZ.js`为`GmeekVercount.js`即可，原先在不蒜子中的数据都会自动同步过来，非常方便。

```
"allHead":"<script src='https://blog.meekdai.com/assets/GmeekVercount.js'></script>",
```

## TOC目录
如果某些文章比较长，里面有很多h1、h2、h3、h4等标题，就可以在右边显示TOC目录，方便导航到对应位置。例如：[markdown测试页面](https://meekdai.github.io/post/markdown-ce-shi-ye-mian.html)

1. 所有文章页添加TOC目录，只需要在config.json文件内添加配置
```
"script":"<script src='https://blog.meekdai.com/assets/GmeekTOC.js'></script>",
```

2. 单个文章页添加TOC目录，只需要在文章最后一行添加如下
```
<!-- ##{"script":"<script src='https://blog.meekdai.com/assets/GmeekTOC.js'></script>"}## -->
```

## 其他
有了插件就可以在基础版的Gmeek框架上玩出很多很多定制化的功能，简单的UI修改也可以通过插件实现，只需要学习一点点前端知识，另外非常欢迎大家一起完善Gmeek，开发出更多的插件。


