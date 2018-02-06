# 1.理解为java的StringBuffer???
from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# 2.读取StringIO
f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

# 3.操作ByteIO
f2 = BytesIO()
f2.write('王琨'.encode('utf-8'))
print(f2.getvalue())