# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/5
@Author      : jim
@File        : [63]不同路径Ⅱ
@Description : 
"""

# 思路1：递归

# 思路2：动态规划，需要判断当前格子是否是障碍
def uniquePathsWithObstacles_DP1(self, obstacleGrid: List[List[int]]) -> int:
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dict = {}
    # 初始化dict
    for (x, y) in [(j, k) for j in range(row + 1) for k in range(col + 1)]:
        if x == row or y == col:
            dict[(x, y)] = 0
        if x == row - 1 and y < col or x < row and y == col - 1:
            dict[(x, y)] = 1
        if x < row and y < col and obstacleGrid[x][y] == 1:
            dict[(x, y)] = 0
    for (x, y) in [(j, k) for j in range(row - 1, -1, -1) for k in range(col - 1, -1, -1) \
                   if obstacleGrid[j][k] != 1 if (j, k) != (row - 1, col - 1)]:
        dict[(x, y)] = dict[(x + 1, y)] + dict[(x, y + 1)]
    return dict[(0, 0)]


# 执行耗时: 48ms, 击败了32.39 % 的Python3用户
# 内存消耗: 14.1MB, 击败了5.00 % 的Python3用户

# 算法有点冗余了，可以改进，有些格子是可以排除，不需要遍历的
def uniquePathsWithObstacles_DP2(self, obstacleGrid: List[List[int]]) -> int:
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dict ,ban = {} , []
    # 初始化dict
    for (x, y) in [(j, k) for j in range(row + 1) for k in range(col + 1)]:
        if x == row or y == col:
            dict[(x, y)] = 0
        if x == row - 1 and y < col or x < row and y == col - 1:
            dict[(x, y)] = 1
        if x < row and y < col and obstacleGrid[x][y] == 1:
            dict[(x, y)] = 0
            if x == 0:
                for y1 in range(y + 1, col):
                    ban.append((0, y1))
            if y == 0:
                for x1 in range(x + 1, row):
                    ban.append((x1, 0))
            if x == row - 1:
                for y1 in range(0, y - 1):
                    ban.append((row - 1, y1))
            if y == col - 1:
                for x1 in range(0, x - 1):
                    ban.append((x1, col - 1))
    for (x, y) in [(j, k) for j in range(row - 1, -1, -1) for k in range(col - 1, -1, -1) \
                   if obstacleGrid[j][k] != 1 if (j, k) != (row - 1, col - 1)]:
        dict[(x, y)] = dict[(x + 1, y)] + dict[(x, y + 1)]
    return dict[(0, 0)]

# 结果反而慢了。。。、
# 执行耗时: 68ms, 击败了7.97 % 的Python3用户
# 内存消耗: 14.2MB, 击败了6.03 % 的Python3用户

# 思路2：自顶向下
def uniquePathsWithObstacles_DP3(self, obstacleGrid: List[List[int]]) -> int:
    row, col = len(obstacleGrid), len(obstacleGrid[0])
    dict = {(0, 0): 1}

    for i in range(row):
        if i > 0:
            dict[(i, -1)] = 0
        else:
            dict[(i, -1)] = 1
        for j in range(col):
            dict[(-1, j)] = 0
            dict[(i, j)] = dict[(i, j - 1)] + dict[(i - 1, j)]
            if obstacleGrid[i][j] == 1:
                dict[(i, j)] = 0
    return dict[(row - 1, col - 1)]
# 这个思路太牛逼了，DP要考虑自顶向下和自底向上两种思路 哪种清晰
# 执行耗时: 28ms, 击败了99.65 % 的Python3用户
# 内存消耗: 13.9MB, 击败了6.03 % 的Python3用户