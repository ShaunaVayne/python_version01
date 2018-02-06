gen = (x * x for x in range(10))
#print(gen)

# for num in gen:
#     print(num)

# def my_function():
#     for i in range(10):
#         yield  i
# print(iter(my_function()))

# def odd() :
#     print('step1')
#     yield (1)
#     print('step2')
#     yield (2)
#     print('step3')
#     yield (3)
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
#
# a = 'hella'
# if a == 'hello' :
#     print('ok')
# else :
#     print('not ok')

def triangles(n) :
    J = [1]
    while True:
        yield J
        J.append(0);
        J = [ J[i -1] + J[i] for i in range(len(J))]
n = 0
for x in triangles(10) :
    print(x)
    n = n + 1
    if n == 10:
        break




