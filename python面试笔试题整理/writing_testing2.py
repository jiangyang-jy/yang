"""计算 n!,例如 n=3(计算 321=6)， 求 10!"""
"""方法一"""
from functools import reduce

a = range(1, 11)
print(reduce(lambda x, y: x*y, a))

"""方法二"""
def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)

a = 10
print(digui(a))

"""方法三"""
a = 10
s = 1
for i in range(1, a+1):
    s = s*i
print(s)

"""已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据"""
a = 0
b = 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b
    a, b = b, a+b