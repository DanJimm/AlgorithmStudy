# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [344]翻转字符串
@Description : 
"""
# 1、双指针遍历
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) <= 1:
        return
    else:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

# 执行耗时: 64ms, 击败了16.76 % 的Python3用户
# 内存消耗: 14.7MB, 击败了48.86 % 的Python3用户