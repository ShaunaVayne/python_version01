# python中的序列化称为picking
import pickle

d = dict(name = 'wangkun', age = 22, sex = 'male')
pickle.dumps(d)
with open('/Users/vayne/myself/tip/data/1.txt','wb') as f :
    pickle.dump(d, f)

# 反序列化
with open('/Users/vayne/myself/tip/data/1.txt','rb') as f:
    none = pickle.load(f)
print(none)
