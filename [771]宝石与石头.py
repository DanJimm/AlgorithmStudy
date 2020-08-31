# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [771]宝石与石头
@Description : 
"""
# J存为一个set，遍历S，查询时间复杂度O(1)，遍历O(n)
def numJewelsInStones(self, J: str, S: str) -> int:
    dict = set(J)
    result = 0
    for i in S:
        if i in dict:
            result += 1
    return result

# 执行耗时: 36ms, 击败了90.72 % 的Python3用户
# 内存消耗: 13.7MB, 击败了47.50 % 的Python3用户