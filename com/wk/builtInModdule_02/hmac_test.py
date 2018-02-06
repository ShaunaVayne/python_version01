#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
import hmac

msg = b'Hello, world!'
key = b'secert'
# (1)param1:盐; param2:明文;param3:加密方式
# (2)传入的盐和明文都必须是byte类型, str编译成byte方式为--> b'str'
h = hmac.new(key, msg, digestmod='MD5')
print(h.hexdigest())



