在博客首页的右上角有一些圆形的按钮，有同学不知道如何配置它们，下面就详细介绍一下配置的方式。

## 站内链接
例如我博客里面的[关于页面](https://blog.meekdai.com/about.html)和[友情链接](https://blog.meekdai.com/link.html)。下面以添加关于页面按钮为示例。

1. 添加config.json配置
```
"singlePage":["about"],
```
2. 添加一个Labels标签为`about`，在你的issue里面写一个文章，然后配置Labels为`about`即可。
3. 手动全局生成一次。

> [!TIP]
> 注意，`about`标签只可以添加给唯一一篇issue，不然会出错
> 如果有多个`singlePage`，则可以这样定义`"singlePage":["link","about"],`
> 如果需要修改或者自定义其他的按钮图标，可以使用`iconList`来配置

## 站外链接
如果你的`about`页面是站外的，或者想定义其他的站外链接，例如我博客里面的[music](https://music.meekdai.com/)。下面以添加music页面按钮为示例。

1. 添加config.json配置
```
"iconList":{"music":"M12.7 0.9L7.3 0.9C6 0.9 4.9 2 4.9 3.3L4.9 10.1C4.5 9.9 4.1 9.8 3.6 9.8C2.1 9.8 0.9 11 0.9 12.4C0.9 13.9 2.1 15.1 3.6 15.1C5 15.1 6.2 13.9 6.2 12.4L6.2 3.3C6.2 2.7 6.7 2.2 7.3 2.2L12.7 2.2C13.3 2.2 13.8 2.7 13.8 3.3L13.8 7.5C13.4 7.3 12.9 7.1 12.4 7.1C11 7.1 9.8 8.3 9.8 9.8C9.8 11.2 11 12.4 12.4 12.4C13.9 12.4 15.1 11.2 15.1 9.8L15.1 3.3C15.1 2 14 0.9 12.7 0.9ZM3.6 13.8C2.8 13.8 2.2 13.2 2.2 12.4C2.2 11.7 2.8 11.1 3.6 11.1C4.3 11.1 4.9 11.7 4.9 12.4C4.9 13.2 4.3 13.8 3.6 13.8ZM12.4 11.1C11.7 11.1 11.1 10.5 11.1 9.8C11.1 9 11.7 8.4 12.4 8.4C13.2 8.4 13.8 9 13.8 9.8C13.8 10.5 13.2 11.1 12.4 11.1ZM12.4 11.1"},
"exlink":{"music":"https://music.meekdai.com"},
```
2. 手动全局生成一次。

> [!TIP]
> 此处`iconList`自定义了图标的SVG，`exlink`定义了外部链接的地址
> `about`和`link`这两个图标的SVG是内置的无需定义`iconList`，其他则需要自己定义

## SVG图标格式
使用`iconList`自定义SVG图标必须是`16px`大小的，建议使用github的`Octicons`图标。

Octicons图标链接：https://primer.style/foundations/icons/#16px
我自己转换的Octicons图标path列表：https://gist.github.com/Meekdai/f6375fe2740428af39d90f1afa678fdc


<!-- ##{"head":"<script src='https://blog.meekdai.com/assets/GmeekTOC.js'></script>"}## -->