# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/6
@Author      : jim
@File        : [647]回文子串
@Description : 
"""

# 思路1：快慢指针
def countSubstrings_double(self, s: str) -> int:
    if not s: return 1
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp = s[i:j + 1]
            tmp_list = list(tmp)
            tmp_list_rev = tmp_list[:]
            tmp_list.reverse()
            if tmp_list == tmp_list_rev:
                res.append(tmp)
    return len(res)
# 执行超时了。。

def countSubstrings_double2(self, s: str) -> int:
    if not s: return 0
    res = []
    L = len(s)
    for i in range(L):
        res.append(s[i:i + 1])
        j = i + 1
        while i > 0 and j < L:
            if s[i] == s[j]:
                res.append(s[i:j + 1])
                i -= 1
                j += 1
            else:
                break
    return len(res)
# 计算错误，没有考虑奇数回文

# 优化代码，把奇数回文考虑进去

# 思路2：动态规划 迭代
# 用dict[i,j] 表示 (i,j)之间围城的字符串是否是回文串 True为是 False表示否
# 1、if i = j,单个字符 True
# 2、if i = j - 1 and s[i] = s[j] True
# 3、else s[i] == s[j] and dict[i+1,j-1]

def countSubstrings_DP3(self, s: str) -> int:
    L = len(s)
    if L <= 1: return 1
    dict, result = [[False for i in range(L)] for j in range(L)], 1
    # 初始化这个dict矩阵
    for i in range(L):
        dict[i][i] = True
    for j in range(1, L):
        for i in range(j + 1):
            if i == j:
                dict[i][j] = True
            elif i == j - 1:
                dict[i][j] = s[i] == s[j]
            else:
                dict[i][j] = s[i] == s[j] and dict[i + 1][j - 1]
            if dict[i][j] == True: result += 1

    return result

# 执行耗时: 412ms, 击败了23.06 % 的Python3用户
# 内存消耗: 22.4MB, 击败了8.21 % 的Python3用户

# 逻辑可以优化
def countSubstrings(self, s: str) -> int:
    L = len(s)
    if L <= 1: return 1
    dict, result = [[False for i in range(L)] for j in range(L)], 0
    for j in range(0, L):
        for i in range(j + 1):
            if i == j:
                dict[i][j] = True
            elif i == j - 1:
                dict[i][j] = s[i] == s[j]
            else:
                dict[i][j] = s[i] == s[j] and dict[i + 1][j - 1]
            if dict[i][j] == True: result += 1

    return result
# 不知道为什么时间反而长了
# 执行耗时: 48ms, 击败了15.24 % 的Python3用户
# 内存消耗: 22.3MB, 击败了15.90 % 的Python3用户




