# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/3
@Author      : jim
@File        : [69]x的平方根
@Description : 
"""
# 思路1：最简单的二分查找，平方根肯定是在1 和 x之间
def mySqrt_simple(self, x: int) -> int:
    if x == 1: return 1
    left, right = 0, x
    while left < right - 1:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid
    return left

# 执行耗时:56 ms,击败了37.62% 的Python3用户
# 内存消耗:13.8 MB,击败了6.63% 的Python3用户

# 思路2，牛顿迭代法
def mySqrt_newtun(self, x: int) -> int:
    if x == 0: return 0
    x0, x1 = float(x), float(x)
    while True:
        x1 = 0.5 * (x0 + x / x0)
        if abs(x0 - x1) < 1e-7:
            break
        x0 = x1

    return int(x1)

# 执行耗时: 48ms, 击败了69.72 % 的Python3用户
# 内存消耗: 13.7MB, 击败了46.44 % 的Python3用户