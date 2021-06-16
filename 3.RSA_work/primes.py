'''
埃氏筛法
（1）先把1删除（现今数学界1既不是质数也不是合数）
（2）读取队列中当前最小的数2，然后把2的倍数删去
（3）读取队列中当前最小的数3，然后把3的倍数删去
（4）读取队列中当前最小的数5，然后把5的倍数删去
（5）如上所述直到需求的范围内所有的数均删除或读取
'''

# 生成一个奇数生成器。
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 过滤掉n的倍数的数。
def not_divisible(n):
    return lambda x: x % n > 0

# 获取当前序列的第一个元素，然后删除后面序列该元素倍数的数，然后构造新序列。
def count():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

# 获取 start 到 stop 之间的 num 个素数
def Primes(start , stop, num):
    primes = []
    k = 0
    for n in count():
        if n > start and n < stop:
            primes.append(n)
            k += 1
        elif n > stop:
            break
        if k==num:
            break
    return primes