# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/24
@Author      : jim
@File        : 各位相加
@Description : 
"""
# 自己只能想到循环和迭代，纯数学解法这么简洁美观，膜拜大佬
def addDigits(self, num: int) -> int:
    if num % 9 == 0 and num != 0:
        return 9
    return num % 9