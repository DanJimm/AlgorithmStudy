# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [58]最后一个单词的长度
@Description : 
"""
# 直接从后往前遍历，再次遇到空格就输出
def lengthOfLastWord(self, s: str) -> int:
    n = 0
    if s == '': return n
    for i in range(len(s) - 1, -1, -1):
        if n != 0 and s[i] == ' ':
            return n
        elif s[i] != ' ':
            n += 1
    return n

# 执行耗时: 36ms, 击败了86.59 % 的Python3用户
# 内存消耗: 13.6MB, 击败了73.99 % 的Python3用户