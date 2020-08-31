# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/29
@Author      : jim
@File        : [657]机器人能否回到原点
@Description : 
"""

#遍历给定数组，相反的方向相互抵消
def judgeCircle(self, moves: str) -> bool:
    count = {'x': 0, 'y': 0}
    for i in moves:
        if i == 'U':
            count['x'] += 1
        elif i == 'D':
            count['x'] -= 1
        elif i == 'L':
            count['y'] += 1
        elif i == 'R':
            count['y'] -= 1
    for i in count:
        if count[i] != 0: return False
    return True

# 执行耗时: 120ms, 击败了5.18 % 的Python3用户
# 内存消耗: 13.6MB, 击败了87.99 % 的Python3用户

#思路2：计数
def judgeCircle_1(self, moves: str) -> bool:
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# 执行耗时: 44ms, 击败了89.97 % 的Python3用户
# 内存消耗: 13.7MB, 击败了79.91 % 的Python3用户