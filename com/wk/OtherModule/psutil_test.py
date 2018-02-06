#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# psutil = process and system utilities; python编写脚本简化运维的工作
import psutil

count = psutil.cpu_count()
print(count)
print(psutil.cpu_count(logical=False))
