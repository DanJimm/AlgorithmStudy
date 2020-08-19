# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/15
@Author      : jim
@File        : [37]解数独
@Description : 
"""

# 思路1：感觉最笨的，把判定数独的方法直接套用
def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row, col, block = [[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]
    empty = []

    def init_board():
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row[i].append(num)
                    col[j].append(num)
                    block[i // 3 * 3 + j // 3].append(num)
                else:
                    empty.append((i, j))

    def useful(x, y):
        list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        return [n for n in list if not n in row[x] and not n in col[y] and \
                not n in block[x // 3 * 3 + y // 3]]

    def helper(iter=0):
        if iter == len(empty):
            return True

        x, y = empty[iter]
        list = useful(x, y)
        print('x ,y list is', (x, y), list)
        for i in list:
            board[x][y] = i
            row[x].append(i)
            col[y].append(i)
            block[x // 3 * 3 + y // 3].append(i)
            if helper(iter + 1):
                return True
            board[x][y] = '.'
            row[x].remove(i)
            col[y].remove(i)
            block[x // 3 * 3 + y // 3].remove(i)
        return False

    init_board()
    helper()


# 执行耗时: 224ms, 击败了49.67 % 的Python3用户
# 内存消耗: 13.8MB, 击败了43.92 % 的Python3用户

# 可以优化代码，不需要useful函数
def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row, col, block = [[str(n) for n in range(1, 10)] for _ in range(9)], \
                      [[str(n) for n in range(1, 10)] for _ in range(9)], \
                      [[str(n) for n in range(1, 10)] for _ in range(9)]
    empty = []

    def init_board():
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row[i].remove(num)
                    col[j].remove(num)
                    block[i // 3 * 3 + j // 3].remove(num)
                else:
                    empty.append((i, j))

    def helper(iter=0):
        if iter == len(empty):
            return True

        x, y = empty[iter]
        b = x // 3 * 3 + y // 3

        for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if i in row[x] and i in col[y] \
                    and i in block[b]:
                board[x][y] = i
                row[x].remove(i)
                col[y].remove(i)
                block[b].remove(i)
                if helper(iter + 1):
                    return True
                board[x][y] = '.'
                row[x].append(i)
                col[y].append(i)
                block[b].append(i)
        return False

    init_board()
    helper()

# 执行耗时: 120ms, 击败了79.79 % 的Python3用户
# 内存消耗: 13.7MB, 击败了85.64 % 的Python3用户