Github地址：[https://github.com/Meekdai/cmder](https://github.com/Meekdai/cmder)

### 为什么要使用它

它看起来非常酷

![2292762868.jpg](https://raw.githubusercontent.com/Meekdai/cmder/master/image/1.jpg)

Markdown高亮，以及背后实时预览功能，随着光标的移动，自动下拉页面。

![748985106.gif](https://raw.githubusercontent.com/Meekdai/cmder/master/image/2.gif)

具备常用代码高亮、折叠、编译的能力。(Python/C/C++/...)

![2439343118.jpg](https://raw.githubusercontent.com/Meekdai/cmder/master/image/3.jpg)

### 说明

Cmder集成强大的命令行工具，可以像用Linux一样使用Windows。

> 使用该软件需要安装 Python

### 安装

1、如果你已经有Git，可以直接通过下面的一条指令安装到你的电脑上。

```
$ git clone https://github.com/Meekdai/cmder.git
```

2、如果电脑上没有安装Git，也许你正需要这个cmder来实现这些功能，那么可以直接通过`Download ZIP`按钮来下载，解压到合适的位置。

###环境变量

必须在环境变量的`Path`中添加`cmder.exe`所在的目录，以及`vim.exe`所在的目录。比如我需要添加的两个路径为`C:\cmder` 和 `C:\cmder\vendor\vim`。 

> 注意解压目录不要包含有中文路径，否则会出现意想不到的错误。

###配置Vundle

在VIM里面，我使用Vundle来管理所有的插件，所以需要先进入到`../cmder/vendor/vim/vimfiles/bundle/`文件夹内把最新的`Vundle`下载下来，当然是在当前目录运行下面这句：

```
git clone https://github.com/VundleVim/Vundle.vim.git
```

成功后，在cmder内运行`vim`指令，进入到`vim`的普通模式下，输入`:PluginInstall`来下载所有的插件。

### 右键设置

可以通过右键，在指定目录打开Cmder。

首先打开具有管理员权限的，快捷键`Ctrl + t`勾选`Run as current user`和`Run as administrator`这两项，然后点`start`开启，然后在命令行输入 :

```
Cmder.exe /REGISTER ALL 1 Cmder.exe /REGISTER ALL 
```
现在在文件夹内右键点击`Cmder here` 就能在`cmder`里进入该目录。

### 快捷键设置
所有的快捷键都放在`../cmder/config/user-aliases.cmd`里面，你可以通过`vim`来编辑它，直接在命令行内输入`kjj`就可以打开编辑它，如果出错了，请参考下文的FAQ。

例如我设置的`gd`为进入到桌面，`vimrc`为打开VIM配置文件，`st`为用sublime Text打开某文件。你可以通过自己的习惯设置一些快捷键。

### FAQ
Q:输入`kjj`提示错误，即`../cmder/config/user-aliases.cmd`内设置的快捷键无效，而`ls`等指令是有用的。
A:这是由于Win10 1703 (Build 15063.11)更新导致，解决办法见[issues #1325](https://github.com/cmderdev/cmder/issues/1325)

Q:右键配置好后，依旧无法进入指定的目录。
A:请配置`cmder.exe`默认为管理员打开。

### License
MIT License

[comment]: # (##{"timestamp":1497112740}##)