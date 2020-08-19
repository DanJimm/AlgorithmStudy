# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/15
@Author      : jim
@File        : [36]有效的数独
@Description : 
"""

# 遍历数组，看是否在横 竖 方块中
def isValidSudoku(self, board: List[List[str]]) -> bool:
    row, col, block = [[] for _ in range(9)], [[] for _ in range(9)], [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                if not num in row[i] and not num in col[j] and \
                        not num in block[i // 3 * 3 + j // 3]:
                    row[i].append(num)
                    col[j].append(num)
                    block[i // 3 * 3 + j // 3].append(num)
                else:
                    return False
    return True

# 执行耗时: 52ms, 击败了75.73 % 的Python3用户
# 内存消耗: 13.5MB, 击败了92.62 % 的Python3用户

# 用dict应该会更快
def isValidSudoku_dict(self, board: List[List[str]]) -> bool:
    row, col, block = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}, \
                      {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}, \
                      {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                if not num in row[i] and not num in col[j] and \
                        not num in block[i // 3 * 3 + j // 3]:
                    row[i].append(num)
                    col[j].append(num)
                    block[i // 3 * 3 + j // 3].append(num)
                else:
                    return False
    return True

# 执行耗时: 44ms, 击败了96.54 % 的Python3用户
# 内存消耗: 13.6MB, 击败了65.74 % 的Python3用户