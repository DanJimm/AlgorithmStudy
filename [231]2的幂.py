# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/19
@Author      : jim
@File        : [231]2的幂
@Description : 
"""

# 练习位运算
# 如果一个数，是2的幂，那么这个数的二进制只能有一个1,所以问题转换为求1的个数
# 1、用x&(-x) 这个方法保留最右边的1，如果 X = x & (-x) 则说明x只有这一个1
def isPowerOfTwo(self, n: int) -> bool:
    if n == 0: return False
    return True if n == n & (-n) else False

# 执行耗时: 40ms, 击败了84.18 % 的Python3用户
# 内存消耗: 13.7MB, 击败了38.05 % 的Python3用户

# 2、删除n最右边的1，看n == 0:
def isPowerOfTwo_1(self, n: int) -> bool:
    if n == 0:return False
    return True if n & (n - 1) == 0 else False

# 执行耗时: 44ms, 击败了64.72 % 的Python3用户
# 内存消耗: 13.6MB, 击败了81.03 % 的Python3用户
# 可以精简到一行
def isPowerOfTwo_2(self, n: int) -> bool:
    return True if n > 0 and n & (n - 1) == 0 else False