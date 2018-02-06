# 模块
from PIL import Image
im = Image.open('/Users/vayne/myself/tip/projects/HelloPython/com/wk/file/fengjing.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((500,270))
im.save('/Users/vayne/myself/tip/projects/HelloPython/com/wk/file/fengjing3.jpg','JPEG')