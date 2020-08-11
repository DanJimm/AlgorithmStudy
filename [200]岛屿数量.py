# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/24
@Author      : jim
@File        : [200]岛屿数量
@Description : 
"""
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集
#  👍 670 👎 0


# 思路1：dfs遍历数组元素，遇到岛屿的时候，判断岛屿水平和竖直方向有没有别的陆地节点
# 定义深度优先算法方法，传入矩阵中为1的点，和当前节点的左边
def dfs(self, grid, r, c):
    grid[r][c] = 0
    # 将处理的坐标值置为0，表示已经处理过
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        if nr > x >= 0 and nc > y >= 0 and grid[x][y] == '1':
            # 点在矩阵范围内，且为1的话，进行处理
            self.dfs(grid, x, y)


def numIslands(self, grid: List[List[str]]) -> int:
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    isand = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                isand += 1
                self.dfs(grid, r, c)

    return isand
# 官方模板效率很高，但是改了原列表，最好还是用副本操作
# 执行用时：76 ms, 在所有 Python3 提交中击败了82.11%的用户
# 内存消耗：14.2 MB, 在所有 Python3 提交中击败了6.67%的用户

# 尝试用dfs模板试一下
class Solution:
    def dfs(self, grid, r, c):
        # 将处理的坐标值置为0，表示已经处理过
        nr , nc = len(grid), len(grid[0])
        for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
            if nr > x >= 0 and nc > y >= 0 and grid[x][y] == '1' and not (x,y) in self.visited:
            # 点在矩阵范围内，且为1的话，进行处理
                self.dfs(grid ,x ,y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        isand = 0
        self.visited = {}
        # 使用了额外的空间记录访问节点，空间复杂度高
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1' and  not (r,c) in self.visited:
                    isand += 1
                    self.dfs(grid,r,c)

        return isand


# 执行耗时: 96ms, 击败了36.70 % 的Python3用户
# 内存消耗: 17.7MB, 击败了6.67 % 的Python3用户

# 思路2：广度优先搜索，迭代法解决，用一个双端队列存储待处理的节点,每次处理把邻居加入右端，然后从左侧弹出一个数值处理
def numIslands(self, grid: List[List[str]]) -> int:
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    isand = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == '1':
                isand += 1
                grid[r][c] = '0'
                neigh = collections.deque([(r,c)])
                while neigh:
                    row, col = neigh.popleft()
                    for x, y in [(row,col-1),(row,col+1),(row-1,col),(row+1,col)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                            grid[x][y] = '0'
                            neigh.append((x,y))

    return isand

# 执行耗时:72 ms,击败了89.99% 的Python3用户
# 内存消耗:14.2 MB,击败了6.67% 的Python3用户