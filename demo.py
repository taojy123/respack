# -*- coding: utf-8 -*-
import os
import respy

# 在开发的时候,你可以使用 make_res 方法将程序中要用到的资源文件打包为一个 py 模块
respy.cls_res()
respy.make_res(os.getcwd() + "\\text.txt")
respy.make_res("pic.jpg")

# 此时当前文件夹下会生成一个 resources.py 文件
# 在程序运行时,上面的资源文件可以删除或移走,只要将这个 resources.py 文件放在目录下即可
# 所以上面这段代码一般在开发过程中只要运行一次,可以写在单独的脚步中,或者直接在 shell 中执行



# 以下为在程序中以 respy 方式调用资源文件的方式

# 首先使用 create_res 方法将 resources.py 中的资源文件释放出来
respy.release_res()
# 此时你可以在 C:\respy_resources\ 目录中看到 text.txt 和 pic.jpg 两个文件
# 现在暂时默认的资源文件释放路径是 C:\respy_resources\,可以看出目前只支持 windows 平台


# 使用 get_res 方法可以获取到文件名对应文件的实际路径
# 例如 respy.get_res("text.txt") 的返回值实际就是 "C:\\respy_resources\\text.txt"
text = respy.get_res("text.txt")
# text 就是 text.txt 文件的路径,可以对其做一些操作,比如以文本文件形式打开它
print open(text).read()

pic = respy.get_res("pic.jpg")
# pic 就是 pic.jpg 文件的路径,可以对其做一些操作,比如使用 PIL 打开查看图片
try:
    from PIL import Image
    im = Image.open(pic)
    im.show()
except:
    print "Please install PIL.."

    