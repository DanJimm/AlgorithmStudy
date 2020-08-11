# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/24
@Author      : jim
@File        : [263]丑数
@Description : 
"""
# 思路1：迭代，依次对 5 3 2做取余运算，有余数就换下一个，如果全部有余数，就不是丑数。然后对除的结果再做运算，直到商为1
def isUgly(self, num: int) -> bool:
    if num == 0:
        return False
    res = num
    while res != 1:
        if res % 5 != 0:
            if res % 3 != 0:
                if res % 2 != 0:
                    return False
                else:
                    res = res / 2
            else:
                res = res / 3
        else:
            res = res / 5
    if res == 1:
        return True

# 执行耗时:40 ms,击败了84.95% 的Python3用户
# 内存消耗:13.6 MB,击败了5.56% 的Python3用户

# 思路2：