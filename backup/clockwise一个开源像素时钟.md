前段时间偶然在网上看到了一个像素时钟的开源项目[clockwise](https://github.com/jnthas/clockwise)。是用ESP32控制一个点阵屏显示当前时间，并且可以替换很多类型的表盘。因为手上有N年前买的ESP32模块，所以只需要在PDD花个20多买个64X64的点阵屏就可以复刻一个。

硬件方面很简单，把ESP32固定在点阵屏的背面，然后按照官方说明焊接好线（蓝黄是电源线，灰色的排线是信号线），烧录固件后，简单的配置就可以看见时钟了。可以看到我的ESP32的USB接口都已经氧化了，也算是物尽其用了。

<img width="544" height="522" alt="Image" src="https://github.com/user-attachments/assets/1ecf1113-ce7c-42b5-885d-c4711330d8a3" />

我比较喜欢这个吃豆子的表盘，因为吃豆子的路径是随机的，每时每刻都是不同的画面，可以盯着看很久，而且实测正常运行的电流比马里奥的小3倍左右。

<img width="411" height="366" alt="Image" src="https://github.com/user-attachments/assets/1a13efaa-610c-48b7-97a0-f711afb1c9b7" />

当然，国内也有很多大佬对这个项目进行了改进，适配了更多的表盘。例如造物计划的[拾光像素](https://www.pixelclock.xyz/)，有非常多有趣的表盘可以选择。

<img width="719" height="549" alt="Image" src="https://github.com/user-attachments/assets/e48933ce-65de-4f28-ae7c-071a0da5274d" />

不过pixelclock需要在QQ群内获取序列号才能使用，每个人限制一个序列号，这确实是一个防止咸鱼党的好办法。