# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/18
@Author      : jim
@File        : [191]位1的个数
@Description : 
"""

# mask左移
def hammingWeight_1(self, n: int) -> int:
    count = 0
    mask = 1
    for i in range(32):
        if mask & n != 0:
            count += 1
        mask <<= 1

    return count

# 执行耗时: 48ms, 击败了26.40 % 的Python3用户
# 内存消耗: 13.6MB, 击败了69.27 % 的Python3用户


# n右移
def hammingWeight_2(self, n: int) -> int:
    count = 0
    while n > 0:
        if 1 & n != 0:
            count += 1
        n >>= 1
    return count

# 执行耗时: 40ms, 击败了76.77 % 的Python3用户
# 内存消耗: 13.5MB, 击败了90.55 % 的Python3用户

# 每次去掉一个1
def hammingWeight_3(self, n: int) -> int:
    count = 0
    while n > 0:
        n &= (n-1)
        count += 1
    return count

# 执行耗时: 36ms, 击败了91.35 % 的Python3用户
# 内存消耗: 13.7MB, 击败了35.07 % 的Python3用户