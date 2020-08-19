# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/14
@Author      : jim
@File        : [51]N皇后_2
@Description : 
"""
# 二刷N皇后
# DFS
def solveNQueens(self, n: int) -> List[List[str]]:
    tmp, result = [], []
    if n == 0: return []
    col, pie, na = [], [], []

    def dfs(x, y, col, pie, na, tmp):
        if x == n - 1 and len(tmp) == n:
            result.append(tmp)
            return

        i = x + 1
        for j in range(n):
            if not j in col \
                    and not i + j in pie and not i - j in na:
                dfs(i, j, col + [j], pie + [i + j], na + [i - j], tmp + [(i, j)])

    i = 0
    for j in range(n):
        if not j in col \
                and not i + j in pie and not i - j in na:
            dfs(i, j, col + [j], pie + [i + j], na + [i - j], tmp + [(i, j)])

    res = []
    for l in range(len(result)):
        tmp1 = []
        for i in range(n):
            tmp2 = ''
            for j in range(n):
                cur = '.' if not (i, j) in result[l] else 'Q'
                tmp2 += cur
            tmp1.append(tmp2)
        res.append(tmp1)
    return res


# 执行耗时: 76ms, 击败了57.34 % 的Python3用户
# 内存消耗: 14.2MB, 击败了9.82 % 的Python3用户

# 很不优雅，优化代码
def solveNQueens_DFS1(self, n: int) -> List[List[str]]:

    result = []
    if n == 0: return []

    def dfs(x, y, col, pie, na, tmp):
        if x == n - 1 and len(tmp) == n:
            result.append(tmp)
            return

        i = x + 1
        for j in range(n):
            if not j in col \
                    and not i + j in pie and not i - j in na:
                dfs(i, j, col + [j], pie + [i + j], na + [i - j], tmp + [(i, j)])

    for j in range(n):
        dfs(0, j, [j], [j], [-j],[(0, j)])

    res = []
    for l in range(len(result)):
        tmp1 = []
        for i in range(n):
            tmp2 = ''
            for j in range(n):
                cur = '.' if not (i, j) in result[l] else 'Q'
                tmp2 += cur
            tmp1.append(tmp2)
        res.append(tmp1)
        return res

# 执行耗时: 72ms, 击败了63.36 % 的Python3用户
# 内存消耗: 14.2MB, 击败了6.83 % 的Python3用户

# 用更优雅的方式处理
def solveNQueens_DFS2(self, n: int) -> List[List[str]]:

    result, tmp = [], []
    col, pie, na = [], [], []

    def dfs(col, pie, na):
        if len(col) == n:
            nonlocal result
            result.append(col)
            return
        for j in range(n):
            if not j in col and len(col) + j not in pie and not len(col) - j in na:
                dfs(col + [j], pie + [len(col) + j], na + [len(col) - j])

    for j in range(n):
        if not j in col and j not in pie and not j in na:
            dfs(col + [j], pie + [len(col) + j], na + [len(col) - j])

    return [['.' * j + 'Q' + '.' * (n - j - 1) for j in list] for list in result]

# 执行耗时: 64ms, 击败了78.21 % 的Python3用户
# 内存消耗: 14.1MB, 击败了14.08 % 的Python3用户
# 可以再优化
def solveNQueens_DFS3(self, n: int) -> List[List[str]]:

    result = []

    def dfs(col, pie, na):
        if len(col) == n:
            nonlocal result
            result.append(col)
            return
        for j in range(n):
            if not j in col and len(col) + j not in pie and not len(col) - j in na:
                dfs(col + [j], pie + [len(col) + j], na + [len(col) - j])

    dfs([],[],[])

    return [['.' * j + 'Q' + '.' * (n - j - 1) for j in list] for list in result]

# 执行耗时: 60ms, 击败了86.24 % 的Python3用户
# 内存消耗: 13.7MB, 击败了99.00 % 的Python3用户