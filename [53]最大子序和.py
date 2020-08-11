# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/9
@Author      : jim
@File        : [53]最大子序和
@Description : 
"""

# 1.子问题 f[i] 表示包含下标为i的数前面的数组的最大子序和，
# 变为不包含num[i] 的 f[i-1] + num[i] 或者 不要f[i-1] 只要num[i] 之间，谁大
# 2、f[i] = max(f[i-1],0) + num[i]\

def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 0: return 0
    dp = nums[:]
    maxNum = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], 0) + nums[i]
        maxNum = max(dp[i], maxNum)
    return maxNum

# 执行耗时: 40ms, 击败了96.91 % 的Python3用户
# 内存消耗: 14.7MB, 击败了6.02 % 的Python3用户