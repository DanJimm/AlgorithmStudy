# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/10
@Author      : jim
@File        : [198]打家劫舍
@Description : 
"""

# 思路1：暴力枚举

# 思路2：动态规划
# 1、子问题
#   问题转换为f[i] 为0-i的盗窃最大值，这个问题有一个小问题，无法直接由f[i-1]得到，因为不能连续偷两个房子
#   是否偷 i 与是否偷（i-1）相关，因此需要增加一个维度，表示是否偷 i
#
# 2、状态定义
#   dp[i][0] 表示不偷i的时候 0-i的最大值
#   dp[i][1] 表示偷i的时候 0-i的最大值

# 3、状态转移方程
#   dp[i][0] = max(dp[i-1][1] , dp[i-1][0])
#   dp[i][1] = dp[i-1][0] + s[i]

def rob_DP1(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = nums[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
        dp[i][1] = dp[i - 1][0] + nums[i]
    return max(dp[n - 1][0], dp[n - 1][1])

# 执行耗时: 44ms, 击败了44.22 % 的Python3用户
# 内存消耗: 13.6MB, 击败了71.59 % 的Python3用户


# 优化方案，不用二维数组记录状态
# 用 dp[i]表示偷到第i个元素的时候的最大金额
# 状态方程为：
# dp[i] = max(dp[i-2] + nums[i],dp[i-1]) 偷i就说明不偷i-1 那就是偷i-2

def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[:2])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return max(dp)

# 执行耗时: 40ms, 击败了70.22 % 的Python3用户
# 内存消耗: 13.6MB, 击败了81.14 % 的Python3用户

# 优化一下比较的方法：
def rob_DP3(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    dp[1] = max(nums[:2])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[n - 1]
# 执行用时：24 ms, 在所有 Python3 提交中击败了99.91%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了25.77%的用户


# 只和前两个有关 只用保留最后两个数值
def rob_DP4(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    a = nums[0]
    b = max(nums[:2])
    for i in range(2, n):
        a, b = b, max(a + nums[i], b)
    return b

# 执行耗时: 40ms, 击败了70.22 % 的Python3用户
# 内存消耗: 13.6MB, 击败了60.58 % 的Python3用户