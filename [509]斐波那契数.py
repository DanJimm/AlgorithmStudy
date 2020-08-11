# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/4
@Author      : jim
@File        : [509]斐波那契数
@Description : 
"""

# 思路1：傻递归
def fib(self, N: int) -> int:
    if N <= 1:
        return N
    else:
        return self.fib(N - 1) + self.fib(N - 2)


# 执行耗时: 772ms, 击败了19.05 % 的Python3用户
# 内存消耗: 13.6MB, 击败了68.93 % 的Python3用户

# 思路2、用dic记录出现过的结果，缩小栈高度
def fib_1(self, N: int) -> int:
    if N == 0: return 0
    dict = [0] * (N + 1)
    dict[1] = 1
    i = 2
    while i <= N:
        dict[i] = dict[i - 2] + dict[i - 1]
        i += 1
    return dict[N]

# 执行耗时: 48ms, 击败了35.47 % 的Python3用户
# 内存消耗: 13.5MB, 击败了89.35 % 的Python3用户

# 优化代码，优雅的生成dic

# 思路3、只记录最近的两个数就可以了 不需要记录list
def fib_3(self, N: int) -> int:
    if N <= 1: return N
    a, b, i = 0, 1, 2
    while i < N:
        a, b = b, a + b
        i += 1
    return (a + b)

# 执行耗时: 40ms, 击败了73.89 % 的Python3用户
# 内存消耗: 13.7MB, 击败了25.44 % 的Python3用户

