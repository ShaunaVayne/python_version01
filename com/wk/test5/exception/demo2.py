#  抛异常
class FooError(ValueError) :
    pass
def foo(s) :
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# foo(0)

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
# bar()

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')