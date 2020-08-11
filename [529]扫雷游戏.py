# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/4
@Author      : jim
@File        : [529]扫雷游戏
@Description : 
"""

# 思路：
# 需要先理清各种转换关系：
#
# 未被挖出的状态：   挖这个点的时候：
# M--地雷             ->X 地雷被挖出，游戏结束 return
#                  / B
# E--空            \  (1 - 8) 数字为周围的地雷数

# 游戏规则：
# 1、点击M M 变成 X ， game over
# 2、点击E -> B 周围没有地雷
#         -> (1 - 8)周围的地雷数量
#
#思路1：BFS 遍历一个节点周围的所有8个相邻节点 ,根据点和周围节点的情况处理
def updateBoard_BFS(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    list, visited = [(click[0], click[1])], {}
    # 初始化待处理的节点列表，和已处理的节点列表
    row, col = len(board), len(board[0])

    def findRelation(p, q, row, col):
        # 定义一个方法，用来找出该节点周围的所有节点，并返回这些节点的list
        nodeList = [(p1, q1) for p1 in [p, p + 1, p - 1] if row > p1 >= 0
                    for q1 in [q, q - 1, q + 1] if col > q1 >= 0]
        nodeList.remove((p, q))
        return nodeList

    while list:
        # 每次取出一个节点
        numLei = 0
        cur_node = list.pop()
        cur_x, cur_y = cur_node[0], cur_node[1]

        # 如果是已访问的节点，跳过
        if (cur_x, cur_y) in visited: continue

        # 先判断该节点是不是雷，是的话把该节点置为 X return
        if board[cur_x][cur_y] == 'M':
            board[cur_x][cur_y] = 'X'
            return board
        # 不是M ，那点击的就是E，把E周围的节点取出来，判断周围有几个雷
        # 如果该节点周围有雷，即该节点最后判定为数字，则周围的节点不添加到list
        elif board[cur_x][cur_y] == 'E':
            nodeList = findRelation(cur_x, cur_y, row, col)
            for i in nodeList:
                x, y = i[0], i[1]
                if board[x][y] == 'M':
                    numLei += 1

            # 该节点周围没有雷，置为B，并把周围节点添加到待处理list
            if numLei == 0:
                board[cur_x][cur_y] = 'B'
                visited[(cur_x, cur_y)] = True
                list += nodeList
            # 该节点周围有雷，该节点置为雷的数量
            else:
                board[cur_x][cur_y] = str(numLei)
    return board

# 执行用时：212 ms, 在所有 Python3 提交中击败了96.34%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了73.68%的用户


