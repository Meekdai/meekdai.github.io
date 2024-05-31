Github由于安全考虑，是不允许使用`iframe`等标签的，而且在issues插入的图片也会自动转换为github的地址。为了文章的多样性，在Gmeek的`v2.19`版本中添加了支持html标签的功能。

## 使用方式

在需要添加html标签的位置使用`code`方式，并且后面紧跟着`Gmeek-html`，然后才是html标签。

### 图片img
```
`Gmeek-html<img src="https://picsum.photos/200">`
```

`Gmeek-html<img src="https://picsum.photos/200">`

### 内嵌框架iframe-网站
```
`Gmeek-html<iframe src="https://music.meekdai.com/#61" width="100%" height="460px" frameborder="0" allowfullscreen="true"></iframe>`
```

`Gmeek-html<iframe src="https://music.meekdai.com/" width="100%" height="460px" frameborder="0" allowfullscreen="true"></iframe>`

### 内嵌框架iframe-歌曲
```
`Gmeek-html<iframe style='border-radius:12px' src='https://open.spotify.com/embed/track/0U3fV7K4WFfVRgLGEAKh3g?utm_source=generator' width='100%' height='152' frameBorder='0' allowfullscreen='' allow='autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture' loading='lazy'></iframe>`
```

`Gmeek-html<iframe style='border-radius:12px' src='https://open.spotify.com/embed/track/0U3fV7K4WFfVRgLGEAKh3g?utm_source=generator' width='100%' height='152' frameBorder='0' allowfullscreen='' allow='autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture' loading='lazy'></iframe>`

### 内嵌框架iframe-视频
```
Gmeek-html<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1604800941&bvid=BV1qm421M7Xs&cid=1557311907&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="460px"></iframe>
```

`Gmeek-html<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1604800941&bvid=BV1qm421M7Xs&cid=1557311907&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="460px"></iframe>`

## 其他
上面仅仅是示例了一些经常会使用到的html标签，其他html标签同样也是支持的，大家可以尝试添加到自己的文章中。



