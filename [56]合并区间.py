# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/23
@Author      : jim
@File        : [56]合并区间
@Description : 
"""

# 首先安装待合并区间的首元素进行排序，这样需要操作的数组就会在一起，然后判断结尾节点就可以了
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0: return []
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []

    pre = intervals.pop(0)
    while intervals:
        cur = intervals.pop(0)
        if pre[1] < cur[0]:
            result.append(pre)
            if len(intervals) == 0:
                result.append(cur)
            pre = cur
        elif cur[0] <= pre[1] <= cur[1]:
            pre = [pre[0], cur[1]]
            if len(intervals) == 0:
                result.append(pre)
        elif len(intervals) == 0:
            result.append(pre)
    if len(result) == 0: result.append(pre)
    return result

# 执行耗时: 56ms, 击败了44.54 % 的Python3用户
# 内存消耗: 14.5MB, 击败了76.49 % 的Python3用户

# 判断太复杂了，可以简化
def merge_1(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []

    for i in intervals:
        if not result or result[-1][1] < i[0]:
            result.append(i)
        elif i[0] <= result[-1][1] <= i[1]:
            result[-1][1] = i[1]

    return result

# 执行耗时: 64ms, 击败了20.39 % 的Python3用户
# 内存消耗: 14.7MB, 击败了16.62 % 的Python3用户