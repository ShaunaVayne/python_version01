#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# psutil = process and system utilities; python编写脚本简化运维的工作
import psutil

count = psutil.cpu_count()
print(count)
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

# 查看进程
print(psutil.pids())    #所有进程
print(psutil.virtual_memory())  #物理内存
print(psutil.swap_memory())     #交换内存

print(psutil.disk_partitions())     #分区信息
print(psutil.disk_usage('/'))

print(181129678848 / 1073741824)