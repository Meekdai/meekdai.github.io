在进行allegro封装建库的时候，我通常会使用FPM这个软件，因为通过这个软件，我就可以用代码来建立PCB封装。FPM这个软件网上可以下载到的版本是`0.0.8`，它内置了许多常用的封装类型，简单的填写一些参数就可以生产一个标准的封装。

除此之外，有些特殊的封装可以自定义，通过编写`skill`的`il`文件来实现。下面是一些常用的语句。

### 注释部分

```
;FPM skill by Meekdai
;Tree:Meekdai/RJ45 Connector
;Desc:W5500
;Vendor:Meekdai
;Count:1
;Datasheet:https://item.szlcsc.com/12651.html
```

### 开头引入

```
sprintf(pName,"W5500")
_PrepareNewSym(pName)
```

### 定义焊盘

```
PadT = _PadTH_Default(2.5 1.7)
PadT1 = _PadTH_Default(2.5 2.5)
PadS = _PadSMFillet(0.72 0.6)
PadN = _PadSM(0.8 2.8) ;圆边焊盘
PadC = _Pad_Slot(4.0 1.8 2.8 0.8)
```

### 创建焊盘

```
_CreatePin(PadT -4.445:-4.355 "1")
_CreatePinMechanical(PadT1 -5.715:1.995)
```

### 使用循环

```
for(i 1 num _CreatePin(PadTH2 pitch*(i-1):0 i)))
```
其中i从1开始，一直到num，每次执行一次

### 使用条件语句

```
if(i==1 _CreatePin(PadTH1 0:0 i) _CreatePin(PadTH2 pitch*(i-1):0 i))
```
如果i等于1就执行第一个语句使用PadTH1，否则用第二个语句使用PadTH2

更多内容可以参考官方文档x:\\Cadence\\SPB_16.x\\doc\\sklangref\\sklangref.pdf

### 创建丝印

```
_Layer(lPkgGeoSilkT) _Rectangle(15.8 20.8 0:0)
_Layer(lPkgGeoSilkT) _Circle(0.254 1.7:1.7)
_Layer(lPkgGeoSilkT) _Line(list(2.5:2.5 -2.5:2.5))
```

### 创建位号

```
_CreateRefValue(pName -3:5 -3:5)
```

### 完成创建

```
_SaveDesign(pName)
```
