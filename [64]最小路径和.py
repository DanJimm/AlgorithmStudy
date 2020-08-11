# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/8
@Author      : jim
@File        : [64]最小路径和
@Description : 
"""

# 思路1：BFS 暴力搜索

# 思路2：DP
# 状态数组：f[i][j] = min(f[i][j-1],f[i-1][j]) + g[i][j]
# 状态转移方程 dp[]

# 自顶向下
def minPathSum_DP1(self, grid: List[List[int]]) -> int:
    x = len(grid)
    if x == 0:
        return 0
    else:
        y = len(grid[0])
        DP = grid[:]
        for i in range(1, y):
            DP[0][i] = DP[0][i - 1] + DP[0][i]
        for j in range(1, x):
            DP[j][0] = DP[j - 1][0] + DP[j][0]
        for i in range(1, x):
            for j in range(1, y):
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + DP[i][j]

    return DP[x - 1][y - 1]


# 执行耗时: 60ms, 击败了65.16 % 的Python3用户
# 内存消耗: 14.9MB, 击败了75.39 % 的Python3用户

# 自底向上
def minPathSum_DP2(self, grid: List[List[int]]) -> int:
    x = len(grid)
    if x == 0:
        return 0
    else:
        y = len(grid[0])
        DP = grid[:]
        for i in range(y - 2, -1, -1):
            DP[x - 1][i] = DP[x - 1][i + 1] + DP[x - 1][i]
        for j in range(x - 2, -1, -1):
            DP[j][y - 1] = DP[j + 1][y - 1] + DP[j][y - 1]
        for i in range(x - 2, -1, -1):
            for j in range(y - 2, -1, -1):
                DP[i][j] = min(DP[i + 1][j], DP[i][j + 1]) + DP[i][j]

    return DP[0][0]

# 执行耗时: 60ms, 击败了65.16 % 的Python3用户
# 内存消耗: 15MB, 击败了59.41 % 的Python3用户

# 优化存储空间，只有一维保存DP状态方程，自顶向下
def minPathSum(self, grid: List[List[int]]) -> int:
    x = len(grid)
    if x == 0:
        return 0
    else:
        y = len(grid[0])
        DP = grid[0][:]
        for j in range(1, y):
            DP[j] = DP[j - 1] + grid[0][j]
        for i in range(1, x):
            DP[0] = DP[0] + grid[i][0]
            for j in range(1, y):
                DP[j] = min(DP[j - 1], DP[j]) + grid[i][j]

    return DP[-1]

# 解答成功:执行耗时: 80ms, 击败了11.22 % 的Python3用户
# 内存消耗: 13.8MB, 击败了96.71 % 的Python3用户
