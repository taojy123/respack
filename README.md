respy    方便快捷的在 Python 中使用资源文件
=====

version 1.0


使用场景
-----------------------------


用 Pyinstaller 可以将 Python 程序打包为单个 exe 文件，发送到没有安装 Python 环境的电脑上直接运行，十分方便好用。

可是一旦你的程序中要用到一些资源文件，比如图片、字体等。你发送给对方的文件就不能只是一个 exe 文件了，必须将这些资源文件一起给对方才能正常使用。

这样一来原来的便捷简洁的特点就不复存在了，所以请使用 respy 来帮你解决这一困扰。

原理其实很简单，首先在开发过程中将资源文件的二进制编码以字符串形式保存在一个 .py 文件中。然后程序中调用资源文件时，将上述编码释放为一个实际文件。



使用说明
-----------------------------


主程序为 respy.py ，将此文件添加到你的程序目录中 import 它即可

respy 主要包含3个方法

make_res(resorce_file) 将资源文件打包到 resources.py 中

release_res() 将 resources.py 中的资源文件释放到默认的资源文件目录

get_res(filename) 根据默认的资源文件目录 返回文件名对应的释放后文件路径

具体见 demo.py 中应用示例




