# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/26
@Author      : jim
@File        : [49]字母异位词分组
@Description : 
"""
# 1.每个单词对应一个list，记录使用字母的数量，list一样的字母，为异位词，放在一起
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 0: return []
    result = []
    dict = {}

    def countLetter(s):
        l = [0] * 26
        for i in s:
            l[ord(i) - 97] += 1
        return str(l)

    for i in strs:
        l = countLetter(i)
        dict.setdefault(l, []).append(i)
    for j in dict:
        result.append(dict[j])
    return result

# 执行耗时: 96ms, 击败了12.58 % 的Python3用户
# 内存消耗: 17.3MB, 击败了19.32 % 的Python3用户

# 2、看了题解，还可以把字符串排序，保存所有可能的异位词
def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
    if len(strs) == 0: return []
    result = []
    dict = {}
    for i in strs:
        l = tuple(sorted(i))
        dict.setdefault(l, []).append(i)
    for j in dict:
        result.append(dict[j])
    return result

# 执行耗时:72 ms,击败了37.37% 的Python3用户
# 内存消耗:17 MB,击败了23.31% 的Python3用户

