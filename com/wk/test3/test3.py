#       装饰器
def log2(text) :
    def log(func) :
        def wrapper(*args, **kw) :
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return log
@log2('execute')
def hha() :
    print('2017-11-1')
hha()