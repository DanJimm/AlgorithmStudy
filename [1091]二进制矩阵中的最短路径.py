# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/17
@Author      : jim
@File        : [1091]二进制矩阵中的最短路径
@Description : 
"""

# 思路1：BFS
def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    row = len(grid)
    if row == 0: return 1
    col = len(grid[0])
    if col == 1 or row == 1:
        return row * row if not 1 in grid else -1
    if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
        return -1

    # BFS
    queue, visited = [(0, 0)], []
    tmp, level = [], 1

    while queue:
        cur_x, cur_y = queue.pop()
        visited.append((cur_x, cur_y))
        tmp += [(x, y) for (x, y) in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), \
                                      (cur_x + 1, cur_y + 1), (cur_x - 1, cur_y + 1), \
                                      (cur_x + 1, cur_y - 1), (cur_x - 1, cur_y - 1), \
                                      (cur_x, cur_y + 1), (cur_x, cur_y - 1)] \
                if 0 <= x < row if 0 <= y < col if grid[x][y] == 0 \
                if not (x, y) in visited]
        if (row - 1, col - 1) in tmp: return level + 1
        if len(queue) == 0:
            if len(tmp) == 0:
                return -1
            else:
                level += 1
                queue, tmp = tmp, []

# 第一版超时了，看看能不能优化

# 改用deque
def shortestPathBinaryMatrix_BFS1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0: return 1
        if row == 1:
            return 1 if not 1 in grid else -1
        if grid[0][0] == 1 or grid[row - 1][row - 1] == 1:
            return -1

        # BFS
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0,0))

        level = 1

        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                for (x, y) in [(i, j) for (i, j) in [(cur_x + 1, cur_y), (cur_x - 1, cur_y),\
                                                     (cur_x + 1, cur_y + 1), (cur_x - 1, cur_y + 1),\
                                                     (cur_x + 1, cur_y - 1), (cur_x - 1, cur_y - 1),\
                                                     (cur_x, cur_y + 1), (cur_x, cur_y - 1)]\
                               if 0 <= i < row if 0 <= j < row if grid[i][j] == 0\
                               if not (i, j) in visited]:
                    if x == y == row - 1:
                        return level + 1
                    queue.append((x, y))
                    visited.add((x, y))
            level += 1
        return -1

# 执行耗时:816 ms,击败了36.83% 的Python3用户
# 内存消耗:14.8 MB,击败了16.16% 的Python3用户
