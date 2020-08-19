# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/13
@Author      : jim
@File        : [547]朋友圈
@Description : 
"""

# 思路1：DFS
def findCircleNum_DFS(self, M: List[List[int]]) -> int:
    def dfs(x, y):
        if M0[x][y] == 1:
            M0[x][y] = '#'
            for y1 in range(col):
                if M0[x][y1] != '#':
                    dfs(x, y1)
            for x1 in range(row):
                if M0[x1][y] != '#':
                    dfs(x1, y)
        else:
            return

    row = len(M)
    col = len(M[0])
    if row * col == 0: return 0

    result, M0 = 0, M[:]
    for x in range(row):
        for y in range(x, col):
            if M0[x][y] == 1:
                result += 1
                dfs(x, y)

    return result

# 执行耗时: 960ms, 击败了5.05 % 的Python3用户
# 内存消耗: 25.3MB, 击败了5.21 % 的Python3用户
# 稍微优化了一下:
def findCircleNum_DFS1(self, M: List[List[int]]) -> int:
    def dfs(x, y):
        if M0[x][y] == 1:
            M0[x][y] = '#'
            for l in range(n):
                if M0[x][l] != '#':
                    dfs(x, l)
                if M0[l][y] != '#':
                    dfs(l, y)
        else:
            return

    n = len(M)
    if n == 0: return 0
    result, M0 = 0, M[:]
    for x in range(n):
        for y in range(x, n):
            if M0[x][y] == 1:
                result += 1
                dfs(x, y)

    return result

# 执行耗时: 860ms, 击败了5.05 % 的Python3用户
# 内存消耗: 25.3MB, 击败了5.21 % 的Python3用户

# 思路2：并查集
def findCircleNum_Union(self, M: List[List[int]]) -> int:
    n = len(M)  # 学生人数

    # 初始化并查集，并查集中记录集合信息
    p = [i for i in range(n)]


    # 定义合并的方法
    def union(p, i, j):
        root_i = find(p, i)
        root_j = find(p, j)
        p[root_j] = root_i


    # 定义find方法
    def find(p ,i):
        if p[i] == i:return i
        root = i
        # 初始化root 并且最终用root记录最终找到的根节点
        while p[root] != root:
            root = p[i]
        # 该循环用来压缩路径
        while p[i] != i:
            x = i
            p[x] = root
            i = p[x]
        return root


    for i in range(n):
        for j in range(i, n):
            if M[i][j] == 1:
                union(p, i, j)

    return len(set([find(p, j) for j in p]))

# 执行耗时:248 ms,击败了50.93% 的Python3用户
# 内存消耗:14 MB,击败了38.77% 的Python3用户