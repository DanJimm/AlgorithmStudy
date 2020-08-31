# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/26
@Author      : jim
@File        : [300]最长上升子序列
@Description : 
"""

'''
1/
 看着题目描述应该用动态规划
 定义状态：DP[i][j] 表示从i- j为上升序列
 状态方程：
 if DP[i][j-1] == 1 and nums[j] > nums[j-1]:
    DP[i][j] = DP[i][j-1] + 1
 else
    DP[i][j] = 1
'''
def lengthOfLIS_son(nums):
    n = len(nums)
    if n <= 0:return n
    dp = [[0]*n]*n
    result = 0
    for i in range(n):
        for j in range(i,n):
            if j == i:
                dp[i][j] = 1
                result = max(result,j - i + 1)
            elif dp[i][j-1] == 1 and nums[j] > nums[j-1]:
                dp[i][j] = 1
                result = max(result, j - i + 1)
            else:
                dp[i][j] = 0
                break
    return result
#理解错题了，题目是要子序列，求成子串了

'''
2/修改状态方程
dp[i]为选i的时候的最长子序列的长度
dp[i] = max(dp[n])+1 if nums[i] > nums[n]
'''
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1: return n
    dp = [1] * n
    result = 0
    for i in range(1, n):
        tmp = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                tmp = max(tmp, dp[j])
        dp[i] = tmp + 1
        result = max(result, dp[i])
    return result

# 执行耗时: 1224ms, 击败了56.88 % 的Python3用户
# 内存消耗: 13.8MB, 击败了35.68 % 的Python3用户