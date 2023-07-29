首先感谢吴川斌的[阿狸狗破戒大师](http://aligou.mr-wu.cn/)，安装的17.2会出现一个细小的问题，经过折腾后，在[论坛](http://bbs.ntpcb.com/read.php?tid-77111.html)中找到了办法，这里对方法进行了改善，以及记录问题，以防下次再碰到。

### 问题描述：
Cadence成功安装后，双击PCB（.brd）文件，不会打开对应的PCB，而是相当于新建了一个文件，非常不方便PCB文件的浏览。

### 问题解决：
在桌面新建一个`Allegro.reg`文件，拷贝以下代码到新建的`reg`文件内，修改allegro.exe以及Capture.exe所在的安装目录，因为下面这个是我的安装地址，注意地址需要使用双`\\`。修改完成后保存，双击运行，重启Allegro，你会发现一切都完美了。

    Windows Registry Editor Version 5.00
    
    [HKEY_CLASSES_ROOT\brd_auto_file\shell\open\command]
    @="C:\\Candence\\Cadence\\Cadence_SPB_17.2-2016\\tools\\bin\\allegro.exe \"%1\""
    
    [HKEY_CLASSES_ROOT\DSN_auto_file\shell\open\command]
    @="C:\\Candence\\Cadence\\Cadence_SPB_17.2-2016\\tools\\bin\\Capture.exe \"%1\""

其实就是往对应的注册表里面添加了末尾的`%1`，不懂这个`%1`可以百度一下，有很清楚的描述。

![7f3b1e89gy1fzpqf9xrurj20uw0itwg1](https://github.com/Meekdai/meekdai.github.io/assets/11755104/02b90a10-3450-43ee-b405-8dace7d044f1)
![7f3b1e89gy1fzpqfmkgxgj20uw0itmyn](https://github.com/Meekdai/meekdai.github.io/assets/11755104/f0d19b75-4960-4303-9e52-e3457581e6bb)

请原谅我安装的时候，拼写错误的`Candence`。

[comment]: # (##{"timestamp":1492169640}##)