# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/23
@Author      : jim
@File        : [242]有效的字母异位词
@Description : 
"""
# 1.第一眼看觉得可以用计数排序解决
def isAnagram(self, s: str, t: str) -> bool:
    letter = [chr(i) for i in range(97, 126)]

    def countNum(str):
        tmp = [0] * 26
        for i in str:
            for j in range(26):
                if i == letter[j]:
                    tmp[j] += 1
        return tmp

    return countNum(s) == countNum(t)

# 执行耗时: 336ms, 击败了5.01 % 的Python3用户
# 内存消耗: 13.8MB, 击败了55.26 % 的Python3用户

# 2.用哈希表统计更快
def isAnagram_1(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in t:
        if not j in dict:
            return False
        else:
            dict[j] -= 1
            if dict[j] < 0: return False
    return True

# 执行耗时: 60ms, 击败了68.81 % 的Python3用户
# 内存消耗: 13.9MB, 击败了39.56 % 的Python3用户