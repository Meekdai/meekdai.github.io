favicon和avatar一般是博客网站必不可少的图标，之前都是采用比较传统的格式制作。特别是`ico`格式，存储空间大，分辨率又低。
```
avatar.jpg   2k
favicon.ico  4.8k
```

而使用SVG（可缩放矢量图形 Scalable Vector Graphics）格式的图标，存储空间将大大减小。
```
avatar.svg   422B
favicon.svg  418B
```

另外得益于`矢量化`，即使图标放大到屏幕这么大也不会有任何模糊。  

## 示例
我的LOGO
`Gmeek-html<img src='https://picsum.photos/200'>`

## 制作
那么如何优雅的把我们的`png`和`jpg`的图片转换为`svg`格式尤其重要。

1. 使用免费在线转换网站，上传我们的图片进行转换。特别注意需要转换后以`path`形式绘制的才行。如下2个网站都是可以的：
[svgcreator](https://svgcreator.com/) 和 [svgtrace](https://svgtrace.com/png-to-svg)

2. 在转换完成后，即可下载svg文件，这时候已经可以使用。不过我们最好还是进行压缩，极致的做法还需要手动删减小数点后的值。
[SVG在线压缩合并工具](https://www.zhangxinxu.com/sp/svgo/)

3. 最后就可以直接在html标签内使用了。
```html
<link rel="icon" href="https://static.meekdai.com/favicon.svg" type="image/svg+xml" />
<img src="https://static.meekdai.com/avatar.svg">
```

当然，如果你的`favicon`和`avatar`使用同一个`svg`那就更好了。另外，图标甚至还能直接使用`svg`设计，可以在[runoob](https://www.runoob.com/svg/svg-tutorial.html)学习用法。

## 其他

Github 官方图标库 [Octicons](https://primer.style/foundations/icons/)
Bootstrap官方图标库[Bootstrap Icon](https://icons.bootcss.com/)
阿里巴巴矢量图标库[iconfont](https://www.iconfont.cn/)
SVG查看编辑器[SVG Viewer](https://www.svgviewer.dev/)
