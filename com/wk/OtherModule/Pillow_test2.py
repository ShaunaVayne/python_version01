#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 模糊显示
from PIL import Image, ImageFilter

image_open = Image.open('/Users/vayne/Pictures/test.jpg')
image_open2 = image_open.filter(ImageFilter.BLUR)
w, h = image_open2.size
image_open2.thumbnail((w//2, h//2))
image_open2.save('test3.jpg','jpeg')
