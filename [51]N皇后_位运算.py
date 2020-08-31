# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/19
@Author      : jim
@File        : [51]N皇后_位运算
@Description : 
"""

# 难点就在于处理攻击区域判定

# 以4皇后为例：
# 初始状态： col pie na = 0000
# 第一次取最后一位1来放，可用范围变成,再取第二位1来放皇后，可用范围变成，
# col         0001                  0101
# pie   ->    0010   -> 1100    ->  1010        ->  0000
# na          0000                  0010


def solveNQueens(self, n: int) -> List[List[str]]:
    col, pie, na = 0, 0, 0
    result, tmp = [], []


    def countP(p):
        count = -1
        while p > 0:
            p >>= 1
            count += 1
        return count


    def dfs(level, col, pie, na, tmp):
        if level >= n and len(tmp) == n:
            result.append(tmp)
            return

        # 求出当前可用的位置：
        bit = (~(col | pie | na)) & ((1 << n) - 1)
        while bit > 0:
            # 取最后一个1出来
            p = bit & -bit
            num = countP(p)
            # 把更新后的占用情况和选择的位置穿到下一层
            dfs(level + 1, col | p, (pie | p) << 1, (na | p) >> 1, tmp + [num])
            bit &= (bit - 1)


    dfs(1, col, pie, na, tmp)
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in result[j]] for j in range(len(result))]

# 执行耗时: 60ms, 击败了86.07 % 的Python3用户
# 内存消耗: 13.9MB, 击败了85.30 % 的Python3用户


