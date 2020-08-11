# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/9
@Author      : jim
@File        : [72]编辑距离
@Description : 
"""

# 1、BFS 遍历，三种路径的三叉树，分别是改变字母，删除元素，插入元素，直到找到目标元素

# 2、DP
# 子问题
# 字符串A 与 B的编辑距离 = A 与 B[:-1]之间的编辑距离 + 1，也等于 A[:-1] 与 B之间的编辑距离 + 1

# 状态定义
# dp[i][j] 表示 A[:i] 和 B[:j] 之间的编辑距离

# 状态转换
# if word1[i] == word2[j]:
#     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
# else:
#     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#
#
def minDistance_DP1(self, word1: str, word2: str) -> int:
    x, y = len(word1), len(word2)
    if x * y == 0: return x + y
    dp = [[0 for i in range(y + 1)] for j in range(x + 1)]
    # dp[0][0] = 0 if word1[0] == word2[0] else 1
    for i in range(x + 1):
        dp[i][0] = i
    for j in range(y + 1):
        dp[0][j] = j
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[x][y]


# 执行耗时: 244ms, 击败了23.54 % 的Python3用户
# 内存消耗: 17.4MB, 击败了37.86 % 的Python3用户
