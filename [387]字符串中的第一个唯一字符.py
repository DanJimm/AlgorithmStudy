# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/24
@Author      : jim
@File        : [387]字符串中的第一个唯一字符
@Description : 
"""
# 1.最简单的用map解决
def firstUniqChar(self, s: str) -> int:
    if len(s) == 0: return -1
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in range(len(s)):
        if dict[s[j]] == 1:
            return j
    return -1

# 执行耗时: 144ms, 击败了49.52 % 的Python3用户
# 内存消耗: 13.7MB, 击败了71.13 % 的Python3用户
