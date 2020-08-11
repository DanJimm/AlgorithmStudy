# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/5
@Author      : jim
@File        : [62]不同路径
@Description : 
"""
# 思路1、递归，转换为子问题,自顶向下
def uniquePaths_recur1(self, m: int, n: int) -> int:
    def helper(x, y):
        if (x, y) == (m - 2, n - 1) or (x, y) == (m - 1, n - 2):
            return 1
        elif x < m - 1 and y < n - 1:
            return helper(x + 1, y) + helper(x, y + 1)
        elif x == m - 1:
            return helper(x, y + 1)
        elif y == n - 1:
            return helper(x + 1, y)

    return helper(0, 0)
# 糟糕的解法，没有保存中间状态，递归会超出深度，需要优化

# 增加一个字典储存中间结果:
def uniquePaths_recur2(m,n):
    if m <= 1 or n <= 1:return 1
    dict = {(m-2,n-1):1,(m-1,n-2):1}
    def helper(x,y):
        # 计算当前节点的路径值
        if x < m - 1 and y < n - 1:
            dict[(x ,y)] = helper(x + 1,y) + helper(x,y + 1)
        elif x == m - 1 and y < n - 2:
            dict[x ,y] = dict[m-1,n-2]
        elif y == n - 1 and x < m - 2:
            dict[x ,y] = dict[m-2,n-1]
        return dict[(x,y)]

    return helper(0,0)

# 还是会超时,性能不够好

# 动态规划，从终点往前倒退
def uniquePaths_DP(self, m: int, n: int) -> int:
    dict = {(m - 1, n - 1): 1}
    for i in range(n - 1):
        dict[(m - 1, i)] = 1
    for i in range(m - 1):
        dict[(i, n - 1)] = 1
    for (x, y) in [(j, k) for j in range(m - 2, -1, -1) for k in range(n - 2, -1, -1)]:
        dict[(x, y)] = dict[x + 1, y] + dict[x, y + 1]
    return dict[(0, 0)]

# 执行耗时:36 ms,击败了90.23% 的Python3用户
# 内存消耗:13.6 MB,击败了75.09% 的Python3用户