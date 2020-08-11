# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/8
@Author      : jim
@File        : [221]最大正方形
@Description : 
"""

# 1、划分子问题
# 2、状态方程
# 3、DP状态转移

# 假设有一个最基本的正方形 边长为2
# 1 1
# 1 1
# 如果边长要变为3 则需要周边都是1
# [1 1] 1
# [1 1] 1
#  1 1  1
# 用dp[i][j]表示 (i ,j )这个点作为右下角，生成正方形的最大边长，即为 左 上 左上三个点的最小值加1
def maximalSquare_DP1(self, matrix: List[List[str]]) -> int:
    row = len(matrix)
    if row == 0: return 0
    col = len(matrix[0])
    maxLen = 0
    dp = matrix[:]
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == '0':
                continue
            else:
                dp[i][j] = min(int(dp[i][j - 1]), int(dp[i - 1][j]), int(dp[i - 1][j - 1])) + 1
            maxLen = max(maxLen, dp[i][j])
    return maxLen * maxLen

# 执行耗时:116 ms,击败了35.76% 的Python3用户
# 内存消耗:14.3 MB,击败了83.38% 的Python3用户