#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# chardet用来检测编码
import chardet

detect = chardet.detect(b'hello world')
print(detect)

detect2 = chardet.detect('离离原上草，一岁一枯荣'.encode('gbk'))
print(detect2)

detect3 = chardet.detect('离离原上草，一岁一枯荣'.encode('utf-8'))
print(detect3)

