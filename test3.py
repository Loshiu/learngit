import math
from functools import reduce
print("给你一个列表 L, 对L进行升序排序并输出排序后的列表。")
# 给你一个列表 L, 对L进行升序排序并输出排序后的列表。
# 例如：L = [8,2,50,3]
# 则输出：[2,3,8,50]
L = [8, 2, 50, 3]
L.sort()
print(L)

print("给你一个字符串 a， 请你输出逆序之后的a。")
# 给你一个字符串 a， 请你输出逆序之后的a。
# 例如：a=‘xydz’
# 则输出：zdyx
a = 'xydz'
print(a[::-1])

print("给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接")
# 给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。
# 例如：a={1:1,2:2,3:3}, 则输出：1,2,3
a = {1: 1, 2: 2, 3: 3}
print(','.join(str(i) for i in sorted(a)))

print("给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。")
# 给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。
# 例如：a=‘xyzwd’
# 则输出:xzd
a = 'xyzwd'
print(a[::2])

print("输出100以内的所有素数，素数之间以一个空格区分")
# 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
# 质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数，这样的数称为质数。
priNum = []
count = 0
for i in range(2, 101):
    for j in range(2, i):
        if i == j:
            break
        if i % j == 0:
            count += 1
    if count == 0:
        priNum.append(i)
    count = 0
print(' '.join(str(i) for i in priNum))
# ============更好的解法============
# 在一般领域，对正整数n，如果用2到  之间的所有整数去除，均无法整除，则n为质数。
# 质数大于等于2 不能被它本身和1以外的数整除
# from math import sqrt
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

print("已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开。")
# 已知矩形长a,宽b,输出其面积和周长，面积和周长以一个空格隔开。
# 例如：a = 3, b = 8
# 则输出：24 22
a = 3
b = 8
print('%d %d' % ((a * b), (a + b) * 2))

print("给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。")
# 给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。
# 例如： L=[0,1,2,3,4]
# 则输出：2
L = [0, 1, 2, 3, 4]
L.sort()
a = len(L) / 2
b = int((len(L) - 1) / 2)
if a % 2 == 1:
    print('%.1f' % ((L[b] + L[b + 1]) / 2))
else:
    print('%.1f' % L[b])

print("给你两个正整数a和b， 输出它们的最大公约数。")
# 给你两个正整数a和b， 输出它们的最大公约数。
# 例如：a = 3, b = 5
# 则输出：1
a = 30
b = 50


# def gcd(a, b):
#     minNum = min(a, b)
#     max = 1
#     for i in range(1, minNum + 1):
#         if a % i == 0 and b % i == 0:
#             max = i
#     return max
# ============更好的解法============


def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a


print(gcd(a, b))

print("给你两个正整数a和b， 输出它们的最小公倍数。")
# 给你两个正整数a和b， 输出它们的最小公倍数。
# 例如：a = 3, b = 5
# 则输出：15
a = 4
b = 6
c = gcd(a, b)
print(a * b // c)

print("给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。")
# 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。
# 例如： L=[2,8,3,50]
# 则输出：2
L = [50, 100, 20, 2]
print(sorted(L))


def f(x, y):
    return x * y


print(reduce(f, L))

c = {"2": 0, "5": 0}


def f1(x):
    while(x % 2 == 0):
        c["2"] += 1
        x /= 2
    while(x % 5 == 0):
        c["5"] += 1
        x /= 5


list(map(f1, L))
print(min(c["2"], c["5"]))
