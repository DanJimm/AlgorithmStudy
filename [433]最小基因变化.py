# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/31
@Author      : jim
@File        : [433]最小基因变化
@Description : 
"""
# 思路1、暴力枚举，列举全部的变化可能，看是否合法，其实算是BFS思想，用一个集合来获取当前的基因可以依次变化得到的基因可能
def minMutation_BFS(self, start: str, end: str, bank: List[str]) -> int:
    # 标志起始基因的依次变化是否合法，如果是false，说明起始基因怎么变都不合法
    num = 0
    origin, tmp1, flag = [start], [], True

    def decideOnece(str1, str2):
        # 判定两组基因是否可以一次变换得到
        equ = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                equ += 1
        return True if equ == len(str1) - 1 else False

    if not end in bank:
        # print('目标不合法')
        return -1
    elif decideOnece(start, end):
        return 1

    while flag:
        flag = False
        for i in origin:
            for j in bank:
                if decideOnece(i, j):
                    flag = True
                    tmp1.append(j)
        origin = [] + tmp1
        if flag == False:
            num = -1
            return num
        else:
            num += 1
        for l in origin:
            if decideOnece(l, end):
                # print('能得到结果')
                num += 1
                return num

# 执行用时：44 ms, 在所有 Python3 提交中击败了43.48%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了16.00%的用户

# 这里检验bank其实重复了，检验过的元素是没必要重复检验的，可以优化代码

def minMutation_BFS2(self, start: str, end: str, bank: List[str]) -> int:
    num = 0
    origin, tmp1 = [start], []

    def decideOnece(str1, str2):
        # 判定两组基因是否可以一次变换得到
        equ = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                equ += 1
        return True if equ == len(str1) - 1 else False

    if not end in bank:
        # print('目标不合法')
        return -1
    elif decideOnece(start, end):
        return 1

    while bank:
        flag = False
        for i in origin:
            for j in bank:
                if decideOnece(i, j):
                    flag = True
                    tmp1.append(j)
                    print('tmp1 is', tmp1)

        origin = [] + tmp1
        bank = [i for i in bank if not i in origin]
        if flag == False:
            num = -1
            return num
        else:
            num += 1
        for l in origin:
            if decideOnece(l, end):
                num += 1
                return num

# 执行耗时:40 ms,击败了69.00% 的Python3用户
# 内存消耗:13.8 MB,击败了12.00% 的Python3用户