# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/14
@Author      : jim
@File        : [200]岛屿数量_2
@Description : 
"""
# 二刷这道题，尝试两种解法，DFS 并查集
# DFS:
def numIslands_DFS1(self, grid: List[List[str]]) -> int:
    def dfs(x, y):
        grid[x][y] = '@'
        nodeList = [(x + x0, y + y0) for (x0, y0) in n
                    if 0 <= x + x0 < row if 0 <= y + y0 < col
                    if grid[x + x0][y + y0] == '1']
        if len(nodeList) == 0:
            return
        for (x1, y1) in nodeList:
            dfs(x1, y1)

    row = len(grid)
    if row == 0: return 0
    col = len(grid[0])
    if col == 0: return 0
    count = 0
    n = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(row):
        for y in range(col):
            if grid[x][y] == '1':
                count += 1
                dfs(x, y)

    return count

# 执行用时：108 ms
# 内存消耗：14.5 MB

# 用并查集试一下
def numIslands_Union(grid):
    row = len(grid)
    if row == 0: return 0
    col = len(grid[0])

    # 初始化所有小岛的并查集，最后一个节点是虚拟节点，用来统一所有的水域
    p = [i for i in range(col * row + 1)]

    def union(p, i, j):
        root_i = find(p, i)
        root_j = find(p, j)
        p[root_j] = root_i

    # 特殊处理连接水域的方法，提升性能
    def union_1(p, i, j):
        p[i] = j

    def find(p, i):
        node = i
        while p[node] != node:
            node = p[node]
        while p[i] != i:
            x = i
            p[i] = node
            i = p[x]
        return node

    # 双指针遍历p，合并相同属性的节点
    for x in range(row):
        for y in range(col):
            if grid[x][y] == '1':
                # 只用看右边和下边的节点，因为上面的已经遍历过了
                for (x2, y2) in [(x + x1, y + y1) for (x1, y1) in [(0, 1), (1, 0)]
                                 if 0 <= x + x1 < row if 0 <= y + y1 < col
                                 if grid[x + x1][y + y1] == '1']:
                    union(p, x * col + y, x2 * col + y2)
            else:
                # 水域都和最后一个虚拟节点相连
                union_1(p, x * col + y, col * row)

    return len(set([find(p, j) for j in p]))


# 执行耗时: 108ms, 击败了20.22 % 的Python3用户
# 内存消耗: 17MB, 击败了6.03 % 的Python3用户