在嵌入式系统中，很多板载芯片都是采用`SPI`总线进行通信，同一`SPI`总线上也运行挂载多个相同或者不同型号的芯片。但是要留意不同型号的芯片的`SPI`通信的时序图，一般会有4种模式。在`micropython`中，初始化`SPI`总线时，通过`phase`和`polarity`配置即可实现这4种模式。

### 四种模式
模式 | CPHA (phase)| CPLO(polarity)
:--: | :--: | :--:
MODE0 | 0 | 0
MODE1 | 1 | 0
MODE2 | 0 | 1
MODE3 | 1 | 1

> CPHA (phase) **0**--第1时钟边缘采样 **1**--第2时钟边缘采样
> CPLO(polarity) **0**--空闲时钟低电平 **1**--空闲时钟高电平

### 常用芯片模式
| 芯片 | 模式 |
| :----: | :----: |
| TMC5130 | MODE3 |
| TMC5160 | MODE3 |
| TMC4671 | MODE3 |
| MAX31865 | MODE1&MODE3 |
| ADS1220 | MODE1 |
| DRV8244 | MODE1 |

### 示例
1. 如下示例配置了`MODE3`，可以与所有支持`MODE3`的芯片通信。
```python
import pyb
spi = pyb.SPI(1, pyb.SPI.MASTER,prescaler=256,phase=1,polarity=1)
```
具体还可参考官方文档 https://docs.micropython.org/en/latest/library/pyb.SPI.html

2. 下图为具体时序示例图
![image2018-11-8 9_41_16](https://github.com/Meekdai/meekdai.github.io/assets/11755104/ed2cda77-af23-40da-ad29-5a41eb5f92e9)
