# 1.写文件示例
try:
    f = open('/Users/vayne/myself/tip/data/2.txt','w')
    f.write('hello world')
except FileNotFoundError as s :
    raise 'iO except : file not found'
finally:
    f.close()

# 2.使用with语句来实现
with open('/Users/vayne/myself/tip/data/2.txt','a') as f:
    for i in range(1,5):
        f.write('hello world' + str(i) + '\n')
