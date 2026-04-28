在给博客添加 [utteranc](https://utteranc.es/) 评论框的时候，发现添加按钮再加载评论框比较友好。但是发现点击后需要隐藏按钮元素，否则会比较奇怪，这个时候就需要通过JS来判断iframe是否成功加载了。

在网上找了一圈，发现 [Iframes, onload, and document.domain](https://humanwhocodes.com/blog/2009/09/15/iframes-onload-and-documentdomain/) 文中给出来比较详细的介绍和方法，但是用在`utteranc`的时候，出现了问题。

`Uncaught TypeError: Cannot read properties of undefined (reading 'attachEvent')` 

定位发现，是由于`iframe`标签都还没有的时候，就去判断`iframe.attachEvent`是不行的。所以我曲线救国，通过定时器读取元素的高度来判断`iframe`标签是否完成了加载，正常情况下，`height`值都应该是存在的，所以代码如下：

```javascript 
int=self.setInterval("iFrameLoading()",200);

function iFrameLoading(){
    var utterances=document.getElementsByClassName('utterances');
    if(utterances.length==1){
        if(utterances[0].style.height!=""){
            int=window.clearInterval(int);
            console.log("utterances Load OK");
        }
    }
}
```

另外我还在官方提了个 [Issue](https://github.com/utterance/utterances/issues/657)，不知道有没有更好的办法来判断。:rofl:


