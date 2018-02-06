# 1.示例
f = open('/Users/vayne/myself/tip/data/1.txt','r')
s = f.read()
print(s)
f.close()

# 2.使用try...finally实现
try :
    f = open('/Users/vayne/myself/tip/data/1.txt','r')
    print(f.read())
finally:
    if f :
        f.close()

# 3.更简洁的写法, with语句实现(python的with语句自动调用close方法,不需要释放资源,与java将流对象写入try括号里道理相同)
with open('/Users/vayne/myself/tip/data/1.txt','r') as f :
    for line in f.readlines():
        print(line.strip())     #strip的作用是把'\n'删掉

# 4.读取二进制文件,如图片, 区别在于用'rb'模式打开
with open('/Users/vayne/myself/tip/data/3.jpg','rb') as f :
    print(f.read())