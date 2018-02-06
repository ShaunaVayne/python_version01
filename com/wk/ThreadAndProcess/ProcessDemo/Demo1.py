# 运行外部进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code',r)

# 如果子进程还需要输入,可通过communicate()方法输入:
