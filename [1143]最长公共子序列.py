# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/11
@Author      : jim
@File        : [1143]最长公共子序列
@Description : 
"""
# DP:
# 1、子问题
#     去掉最后一个字符的字符串和另一个字符串的最大子串，在增加一个字符的时候，最大子串值得变化
#     只有当两个字符串的最后一个字符，是另一个字符串中未包含在子串中的字符的时候，长度会变化
# 2、状态定义：dp[i][j] 表示字符串a 0-i 和 字符串b 0-j 之间，最长的子串长度
#   if text1[i] == text2[j]
#       dp[i][j] = dp[i-1][j-1] + 1
#   else dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#
# 3、状态转移方程
#   初始化状态方程
#   dp[0][0] = 1 if text1[0] == text2[0] else 0
#   for i in range(x):
#       if dp[i-1][0] == 1:dp[i][0] = 1
#       elif dp[i-1][0] == 0 and text1[i] == text2[0]:
#           dp[i][0] = 1
#
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    x, y = len(text1), len(text2)
    if x * y == 0: return 0
    # 初始化dp
    dp = [[0 for _ in range(x)] for _ in range(y)]
    dp[0][0] = 1 if text1[0] == text2[0] else 0
    for i in range(1, x):
        if dp[0][i - 1] == 1:
            dp[0][i] = 1
        elif dp[0][i - 1] == 0 and text1[i] == text2[0]:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for j in range(1, y):
        if dp[j - 1][0] == 1:
            dp[j][0] = 1
        elif dp[j - 1][0] == 0 and text1[0] == text2[j]:
            dp[j][0] = 1
        else:
            dp[j][0] = 0
    for i in range(1, y):
        for j in range(1, x):
            if text1[j] == text2[i]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[y - 1][x - 1]

# 执行耗时:420 ms,击败了93.60% 的Python3用户
# 内存消耗:22.3 MB,击败了17.97% 的Python3用户

# 初始化dp可以优化
def longestCommonSubsequence_DP2(self, text1: str, text2: str) -> int:
    x, y = len(text1), len(text2)
    if x * y == 0: return 0
    # 初始化dp
    dp = [[0 for _ in range(x + 1)] for _ in range(y + 1)]
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            if text1[j - 1] == text2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[y][x]

# 执行耗时: 492ms, 击败了53.48 % 的Python3用户
# 内存消耗: 22.4MB, 击败了13.33 % 的Python3用户
