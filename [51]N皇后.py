# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/30
@Author      : jim
@File        : [51]N皇后
@Description : 
"""
# 思路1、回溯，穷举，依次放下每一个皇后，校验是否会和前面的棋子攻击
def solveNQueens_recur(self, n: int) -> List[List[str]]:
    if n <= 0:
        return None

    # 初始化数据
    coo, result = [(0, -1)], []

    # 判断是否在前序皇后的攻击范围
    def decide_atack(coo_cur, coo_list):
        atack_list = []
        # cur存储当前皇后坐标，list是已有的皇后的坐标
        for i in coo_list:
            atack_list += calAtack(i)
        if coo_cur in atack_list:
            return True
        else:
            return False

    def calAtack(coo_cur):
        # 计算当前已有节点的攻击范围
        atack_cur = []
        row = coo_cur[0]
        col = coo_cur[1]
        for i in range(row + 1, n):
            atack_cur.append((i, col + (i - row)))
            atack_cur.append((i, col - (i - row)))
            atack_cur.append((i, col))
        return atack_cur

    # 在棋盘row,col放下棋子
    def putQ(row, col, coo_list, coo):
        if row < 0:
            return
        elif row >= n:
            coo += coo_list
            return
        elif col >= n:
            if not coo_list: return
            last = coo_list.pop()
            putQ(row - 1, last[1] + 1, coo_list, coo)

        elif decide_atack((row, col), coo_list):
            putQ(row, col + 1, coo_list, coo)

        else:
            putQ(row + 1, 0, coo_list + [(row, col)], coo)

    # 按照期盼模式输出
    def output(coo_list):
        res = []
        if not coo_list:
            return
        for i in range(n):
            row = ''
            for j in range(n):
                if (i, j) in coo_list:
                    row += 'Q'
                else:
                    row += '.'
            res.append(row)
        return res

    # main函数，不断寻找可能的结果
    while coo:
        node = coo.pop()
        row, col = node[0], node[1] + 1
        coo_tmp = coo[:]
        coo = []
        putQ(row, col, coo_tmp, coo)
        if coo:
            result.append(output(coo))
    return result

# 时间复杂度应该是O(n!)，可能不止这么多，因为我设计的计算攻击范围的方案不太好，计算量比较大
# 执行耗时:1684 ms,击败了5.06% 的Python3用户
# 内存消耗:15.6 MB,击败了5.13% 的Python3用户

# 优化代码，优化攻击判定
def solveNQueens_recur1(self, n: int) -> List[List[str]]:
    if n == 0:
        return None

    coo, result = [(0, -1)], []

    def decide_atack(coo_cur, coo_list):
        # cur存储当前皇后坐标，list是已有的皇后的坐标
        for i in coo_list:
            if calAtack(coo_cur, i):return True
        return False

    def calAtack(coo_cur, coo_bef):
        # 计算两个节点是否相互攻击
        row, col = coo_cur[0], coo_cur[1]
        row1, col1 = coo_bef[0], coo_bef[1]
        return True if row == row1 or col == col1 or row + col == row1 + col1 or row - col == row1 - col1 \
            else False

    # 在棋盘row,col放下棋子
    def putQ(row, col, coo_list, coo):
        if row < 0:
            return
        elif row >= n:
            coo += coo_list
            return
        elif col >= n:
            if not coo_list: return
            last = coo_list.pop()
            putQ(row - 1, last[1] + 1, coo_list, coo)

        elif decide_atack((row, col), coo_list):
            putQ(row, col + 1, coo_list, coo)

        else:
            putQ(row + 1, 0, coo_list + [(row, col)], coo)

    def output(coo_list):
        res = []
        if not coo_list:return []
        for i in range(n):
            row = ''
            for j in range(n):
                if (i, j) in coo_list:
                    row += 'Q'
                else:
                    row += '.'
            res.append(row)
        return res

    while coo:
        node = coo.pop()
        row ,col = node[0] ,node[1] + 1
        coo_tmp = coo[:]
        coo = []
        putQ(row, col, coo_tmp, coo)
        if coo:
            result.append(output(coo))
    return result

# 执行用时：172 ms, 在所有 Python3 提交中击败了12.69%的用户
# 内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.13%的用户

# 思路2：看了优秀题解，DFS遍历的方式解决：
def solveNQueens_dfs(self, n: int) -> List[List[str]]:
    result = []

    # 定义方法，传入已有的节点列表，和已有的攻击区域
    def DFS(list, pie, na):
        p = len(list)
        # 巧妙的处理，保证每次循环的都是第n行
        if p == n:
            # 遍历完了矩阵
            result.append(list)
            return None
        for q in range(n):
            if q not in list and p - q not in na and p + q not in pie:
                DFS(list + [q], pie + [p + q], na + [p - q])

    DFS([], [], [])
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in j] for j in result]


# 执行耗时: 64ms, 击败了78.04 % 的Python3用户
# 内存消耗: 13.8MB, 击败了94.87 % 的Python3用户