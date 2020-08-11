# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/27
@Author      : jim
@File        : [50]Pow(x,n)
@Description : 
"""

# 思路1：暴力循环，有n个数就乘n次，时间复杂度O(n)
def myPow(self, x: float, n: int) -> float:
    if n == 0: return 1
    result = 1
    if n > 0:
        for i in range(n):
            result = result * x
        return result
    else:
        for i in range(-n):
            result = result * x
        return 1 / result

# submit不通过，n过大的时候会超时

# 思路2、分治的思想，简化问题，x^n = x^(n/2) * x^(n/2),因此，可以递归简化为求子问题的答案，但是要注意处理边界条件
def myPow_recur(self, x: float, n: int) -> float:
    def quickMyPow(n):
        if n == 0:
            return 1
        y = quickMyPow(n // 2)
        if n % 2 == 1:
            return y * y * x
        else:
            return y * y

    if n > 0:
        return quickMyPow(n)
    else:
        return 1 / quickMyPow(-n)

# 这个代码没写出来不应该，子问题和边界条件没有理清楚
# 执行耗时:40 ms,击败了74.60% 的Python3用户
# 内存消耗:13.7 MB,击败了8.33% 的Python3用户

# 改进代码：
def myPow_recur1(self, x: float, n: int) -> float:
    def quickMyPow(n):
        if n == 0:
            return 1
        y = quickMyPow(n // 2)
        return y * y * x if n % 2 == 1 else y * y
    return quickMyPow(n)  if n > 0 else 1/quickMyPow(-n)

