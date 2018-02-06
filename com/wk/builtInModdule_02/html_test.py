#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 编写一个搜索引擎, 第一步即爬虫j将目标网站的页面抓下来; 第二步: 解析这个html页面
# 如何解析HTML? html本质是xml的子集, py提供了htmlParser解析html
from html.parser import HTMLParser


class myHtmlParser(HTMLParser):
    def error(self, message):
        print('msg: %s' % message)
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_data(self, data):
        print(data)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    def handle_comment(self, data):
        print('<!--', data ,'-->')
    def handle_entityref(self, name):
        print('&%s;' % name)
    def handle_charref(self, name):
        print('&#%s;' % name)


parser = myHtmlParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')




