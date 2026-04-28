通过python的 `pip install pyopengl`指令在win10 64位的系统上安装后，运行官方茶壶的例子，会出现如下报错：

```python
OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInitDisplayMode, check for bool(glutInitDisplayMode) before calling
OpenGL.error.NullFunctionError: Attempt to call an undefined function
```

这些都是因为通过pip安装的版本是32位导致的，我看了很多网上的解决办法说是手动下载64位的包安装即可解决。但是我按要求下载64位的包后，通过 `pip install XXX.whl`本地安装的方式，却提示我64位的pyopengl已经安装，无需重复安装。让我在这个坑里面跳了好久没跳出来。

最后的解决办法是，你需要先卸载已经安装好的pyopengl，再手动安装一下才行。所以在这里记录一下，以便有其他人遇到同样的坑。
这里给一下手动下载的地址：[pyopengl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl)

也顺便贴一下官方的测试茶壶代码：

```python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
def drawFunc():
    #清楚之前画面
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 5, 5, 0)   #(角度,x,y,z)
    glutWireTeapot(0.5)
    #刷新显示
    glFlush()
    
#使用glut初始化OpenGL
glutInit()
#显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
#窗口位置及大小-生成
glutInitWindowPosition(0,0)
glutInitWindowSize(400,400)
glutCreateWindow(b"first")
#调用函数绘制图像
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
#主循环
glutMainLoop()
```

python的pyopengl配合pygame还是很香的，有空多学习学习。下面放一张最近做的一个小东西，具体是干嘛用的，之后应该会有文章详细介绍。@(滑稽)

![pyeuler](https://github.com/Meekdai/meekdai.github.io/assets/11755104/3d227e8c-77ef-4044-9331-e2d7a77af4c2)

[comment]: # (##{"timestamp":1647152153}##)