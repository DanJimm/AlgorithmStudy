# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [14]最长公共前缀
@Description : 
"""
# 1.一位一位的比较
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0: return ''
    if len(strs) == 1: return strs[0]
    ans = ''
    n = len(strs)
    j, i = 0, 0
    while strs[i]:
        if j >= len(strs[i]):
            return ans
        else:
            pre = strs[i][j]
        for i in range(1, n):
            if j < len(strs[i]) and strs[i][j] == pre:
                continue
            else:
                return ans
        ans += pre
        j += 1
        i = 0
    return ans

# 执行耗时: 48ms, 击败了36.27 % 的Python3用户
# 内存消耗: 13.8MB, 击败了24.29 % 的Python3用户

# 用Trie试一下
def longestCommonPrefix(self, strs: List[str]) -> str:
    p = {}
    for i in strs:
        node = p
        for j in i:
            node = node.setdefault(j, {})
        node['#'] = '#'
    node = p
    ans = ''
    while '#' not in node:
        index, tmp = 0, ''
        for x in node:
            tmp += x
            index += 1
        if index == 1:
            ans += tmp
            node = node[tmp]
        else:
            return ans
    return ans

# 执行耗时: 40ms, 击败了81.71 % 的Python3用户
# 内存消耗: 13.6MB, 击败了88.10 % 的Python3用户