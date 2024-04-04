这篇文章详细说一下目前Gmeek支持的亮暗主题配置方式，以及后续待改进之处。

## 手动模式（默认）
这种模式就是当访问者第一次打开博客页面时，呈现的是亮主题。访问者可以通过页面右上角的按钮随意切换（亮/暗/跟随系统），当切换过后，会自动在浏览器存储目前的选择，之后访问者用同一浏览器再打开博客任何页面，则自动为上次选择的模式。
```
"themeMode":"manual",
"dayTheme":"light",
"nightTheme":"dark",
```

## 固定模式
设置`themeMode`为`fix`，`dayTheme`定义的就是想要固定的主题，可以定义为`light`则永远为亮主题，用户无法切换，定义为`dark`则永远为暗主题。而`nightTheme`定义的就是`utterances`评论框的永久固定主题。

### 固定亮主题
```
"themeMode":"fix",
"dayTheme":"light",
"nightTheme":"github-light",
```

### 固定暗主题
```
"themeMode":"fix",
"dayTheme":"dark",
"nightTheme":"dark-blue",
```

这里提到的亮暗主题可以查看[github官方](https://github.com/settings/appearance)支持的主题，这里都支持
- 亮主题：`light` `light_high_contrast` `light_colorblind ` `light_tritanopia `
- 暗主题：`dark` `dark_high_contrast` `dark_colorblind` `dark_tritanopia` `dark_dimmed`

而[utterances](https://utteranc.es/)评论框的主题选择有
```
github-light
github-dark
preferred-color-scheme
github-dark-orange
icy-dark
dark-blue
photon-dark
boxy-light
gruvbox-dark
```

## 其他
目前做到的就是这些功能，可以定义的主题模式有限，但还是有一些选择的。可以优化的地方还要很多，如果有其他主题方面的需求或者建议欢迎一起讨论和完善。

1、固定跟随系统切换目前还没有实现
2、手动模式目前访问者第一次打开页面是亮主题，是否需要实现第一次打开是暗主题或者是跟随系统？
