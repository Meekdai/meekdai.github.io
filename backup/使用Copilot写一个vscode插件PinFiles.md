这个插件的名称叫`PinFiles`，意思就是永久固定文件到`vscode`的侧边栏中，当然你可以很方便的添加和删除。
开源地址：[PinFiles](https://github.com/Meekdai/PinFiles)
插件市场：[marketplace](https://marketplace.visualstudio.com/items?itemName=Meekdai.pinfiles)

事情是这样的，我在用vscdoe的时候，经常需要打开某些固定的文件。例如自己记录的linux常用指令`linux.md`文件，或者编译`micropython`固件时候，经常用到的指令记录`make.py`，等等很多。这样在用`vscode`打开项目文件夹后，还需要再重新打开这些文件，非常的麻烦。

所以我在`vscode`插件中找了一圈没有找到合适的，在[V2EX](https://www.v2ex.com/t/996615)上提问也没有合适的答案。所以想要自己手搓一个，但是对于没有开发过`vscode`插件的我来说，可能需要比较长的时间。但是当我用上了`Copilot with Bing Chat`，哈哈，一问一答的方式，2个小时就完成了，并且发布到了`marketplace`。

下面大致记录一下过程：
1、参考官方文档[Your First Extension](https://code.visualstudio.com/api/get-started/your-first-extension) 安装`nodejs`还有一些依赖等，然后运行`yo code`就可以轻松创建一个插件框架。需要注意的是`package.json`中的`"engines": {"vscode": "^1.30.0"}`版本，必须低于你当前使用的版本，不然调试的时候不会正确加载。

2、使用`Copilot with Bing Chat` 描述你想要的功能，然后一步一步优化，解决bug等等。

3、等功能都差不多后，根据[VSCode 插件发布](https://zhuanlan.zhihu.com/p/504218497) 就可以发布了，这里面会有一些权限等问题，简单google一下就可以解决。

4、最后我把工程同步到`github`上，然后用指令`vsce publish patch` 就会自动升级版本并且上传发布，过几分钟就可以搜索到了。

后续会使用的链接：  
> Azure DevOps 组织的[tokens](https://dev.azure.com/meekdai/_usersSettings/tokens)  
> 上传发布进度查看[marketplace](https://marketplace.visualstudio.com/manage/publishers/Meekdai?auth_redirect=True)  


