#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image

image_open = Image.open('/Users/vayne/Pictures/Saved Pictures/test.jpg')

# 获得尺寸
w, h = image_open.size
print('Original image size: %sx%s' % (w, h))
# 缩放50%
image_open.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' %(w//2, h//2))
# 缩放后的图片保存
image_open.save('test2.jpg','jpeg')