#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 解析xml
# 操作xml的两种方法:dom和sax:
# dom会把xml全部读到内存,解析为数,占用内存大,优点是可以遍历树的每个节点;
# sax是流模式,边读边解析,占用内存小,解析快,缺点是要自己处理事件.
from pyexpat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s, attrs: %s' %(name, str(attrs)))
    def end_element(self, name):
        print('sax: end_element: %s' % name)
    def char_data(self, text):
        print('sax: char_data: %s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

sax_handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = sax_handler.start_element
parser.EndElementHandler = sax_handler.end_element
parser.CharacterDataHandler = sax_handler.char_data
parser.Parse(xml)

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('test something')
L.append(r'</root>')
print(''.join(L))
