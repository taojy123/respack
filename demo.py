import os
import respy


# ======== Base Usage ========

respy.set('pic.jpg')

# ...
# you can remove `pic.jpg` after respy.set() run once
# ...

path = respy.get('pic.jpg')

try:
    print('install Pillow to see this image')
    from PIL import Image
    im = Image.open(path)
    im.show()
except ImportError:
    print(path)



# ======== Advance Usage ========

# 1. custom target name
respy.set('./pic.jpg', 'mypic')
path = respy.get('mypic')
print(path)

# 2. custom resources root dir
respy.set('./pic.jpg')
path = respy.get('pic.jpg', resources_dir='./res_root/')
print(path)

# 3. use cache
respy.set('pic.jpg')
path = respy.get('pic.jpg', cached=True)
path = respy.get('pic.jpg', cached=True)  # will not release resource files again
print(path)



