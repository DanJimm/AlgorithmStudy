# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/19
@Author      : jim
@File        : [190]颠倒二进制位
@Description : 
"""

# 1、每次取n最后一位，给新的int，并且每次int << 1
def reverseBits(self, n: int) -> int:
    new = 0
    for i in range(31, -1, -1):
        new = (new << 1) + (n & 1)
        n >>= 1
    return new

# 执行耗时: 44ms, 击败了60.07 % 的Python3用户
# 内存消耗: 13.7MB, 击败了52.13 % 的Python3用户

