# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/15
@Author      : jim
@File        : [70]爬楼梯-2
@Description : 
"""
# 再刷爬楼梯
# 傻递归
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# 超时

# 记忆化搜索,自底向上
def climbStairs_list(self, n: int) -> int:
    stair = [0] * (n + 1)
    for i in range(n + 1):
        if i <= 2:
            stair[i] = i
        else:
            stair[i] = stair[i - 1] + stair[i - 2]
    return stair[n]

# 执行耗时: 40ms, 击败了65.59 % 的Python3用户
# 内存消耗: 13.7MB, 击败了43.43 % 的Python3用户

# 递归，自顶向下
def climbStairs_recur(self, n: int) -> int:
    stair = {0: 0, 1: 1, 2: 2}

    def helper(n):
        if n in stair:
            return stair[n]
        stair[n] = helper(n - 1) + helper(n - 2)
        return stair[n]

    return helper(n)

# 执行耗时: 44ms, 击败了39.02 % 的Python3用户
# 内存消耗: 13.8MB, 击败了13.79 % 的Python3用户

# DP
def climbStairs_DP(self, n: int) -> int:
    if n <= 2: return n
    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, a + b
    return b

# 执行耗时: 44ms, 击败了39.02 % 的Python3用户
# 内存消耗: 13.8MB, 击败了15.92 % 的Python3用户