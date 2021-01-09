"""练习一：统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,
-9, -4, -5, 8]"""
"""解法一"""
li = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
a = [x for x in li if x > 0]
b = [x for x in li if x < 0]
print(f"队列正数有：{len(a)}，负数有:{len(b)}")

"""解法二"""
n = 0
m = 0
for i in li:
    if i > 0:
        n += 1
    elif i < 0:
        m += 1
print(f"队列正数有：{n}，负数有:{m}")


"""练习二：字符串 "axbyczdj"，如何得到结果“abcd”"""
"""解法一"""
s = "axbyczdj"
print(s[::2])

"""解法二"""
c = []
for i in range(len(s)):
    if i % 2 == 0:
      c.append(s[i])
print("".join(c))

# str.join(sqa)的应用
# seq = ('j', 'i', 'a', 'n', 'g')
# l = ['y', 'a', 'n', 'g']
# print("-".join(seq), "-".join(l))


"""练习三：已知一个字符串为“hello_world_yoyo”, 如何得到一个队列
["hello","world","yoyo"]"""
a = "hello_world_yaya"
ya = a.split("_", 2)#str.split(s, num)[n]是一个list对象,,,s表示用那个字符分割，num分割的次数，n索引取哪一个；
print(ya)


"""练习四：已知一个数字为 1，如何输出”0001”"""
nums = 1
print("%.4d"%nums)
#格式化输出f是控制小数位数
#s控制左右对齐
#d前面会补0


"""练习五：已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
[3, 5, 1, 7]"""
li = [1, 3, 5, 7]
li.insert(3, li[0])
print(li[1:])


"""练习六：已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9"""
a = 9
b = 8
a, b = b, a
print(f"a交换后的值为{a},b交换的值为{b}")


"""练习七：打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋3 的三次方。"""
for i in range(100, 999):
    s = str(i)
    summ = int(s[0])**3 + int(s[1])**3 + int(s[2])**3
    if i == summ:
        print(i, end='\t')
print()


"""练习八：如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备
数。 例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
3 个数相加，
1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28
外，其余 5 个数相加，1+2+4+7+14=28。
那么问题来了，求 1000 以内的完全数有哪些？"""
for i in range(1, 1000):
    summm = 0#放在循环的上一层就行，这种情况不能放i的上面，不能跨两层；
    for j in range(1, i):
        if i % j == 0:
            summm += j
    if i == summm:
        print(i, end='\t')
print()

"""练习九：用 python 写个冒泡排序a = [1, 3, 10, 9, 21, 35, 4, 6]"""
a = [1, 3, 10, 9, 21, 35, 4, 6]
for i in range(1, len(a)):
    for j in range(1, len(a)-i+1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
print(a)


"""练习十：已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
 按从小到大排序
 按从大大小排序
 去除重复数字"""
a = [1, 3, 6, 9, 7, 3, 4, 6]
print(sorted(a))
print(sorted(a, reverse=True))
print(set(a))
