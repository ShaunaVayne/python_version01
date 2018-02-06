# collections是py内建的一个集合模块,提供集合类

# 1.namedtuple,用于自定义tuple对象,并规定tuple的个数
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

p = namedtuple('point', ['x', 'y'])
p1 = p(1, 2)
print(p1.x)
print(p1.y)
# 如上类似定义一个坐标, 若定义一个圆则如下
c = namedtuple('cricle', ['x', 'y', 'r'])
# 可以验证p对象是tuple的子类,namedtuple具有tuple的不变性,根据属性来引用
print(isinstance(p1,tuple))
print('-------------------------------------------')

# 2.deque:
# 使用list来存储数据, 根据索引访问元素很快, 但是因为list是线性存储, 数据量大,增删效果不好,
# deque是为了高效实现增删操作的双向列表, 类似java的linkendlist的链表结构,适用于队列和栈
d = deque(['1', '2', '3'])
d.append('x')
d.appendleft('y')
print(d)
print('-------------------------------------------')

# 3.defaultdict
# 使用dict时,如果key不存在则抛异常,defaultdict即给默认值
d2 = defaultdict(lambda: 'default')
d2['a'] = '100'
print(d2['a'])
print(d2['b'])
print('-------------------------------------------')

# 4.OrderedDict
# 使用dict时,key无序.对dict做迭代时,无法确定key的顺序,使用OrderedDict则保证key有序
d3 = dict([('a' , 1), ('b' , 2), ('c' , 3)])
print(d3)
d4 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d4)
# OrderedDict的key会按照插入的顺序排列,而不是key本身排序
d5 = OrderedDict()
d5['k'] = 1
d5['x'] = 2
d5['y'] = 5
print(d5.keys())
# OrderedDict可以实现一个先进先出的队列特性(FIFO),若容量超出限制, 会先删除最早添加的key, 代码如下
class QueueDemo(OrderedDict) :
    def __init__(self, capacity):
        super(QueueDemo, self).__init__()
        self.capacity = capacity
    def __setitem__(self, key, value):
        containkey = 1 if key in self else 0
        if len(self) - containkey >= self.capacity :
            last = self.popitem(last= False)
            print('remove:', last)
        if containkey :
            del self[key]
            print('set:', (key, value))
        else :
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
print('-------------------------------------------')

# 5.counter 计数器
# Counter实际上也是dict的一个子类
c = Counter()
for ch in "wwwwangkun":
    c[ch] += 1
print(c)




