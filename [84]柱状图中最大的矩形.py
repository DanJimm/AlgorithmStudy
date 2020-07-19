# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/18
@Author      : jim
@File        : [84]柱状图中最大的矩形
@Description : 
"""
# 思路1：暴力枚举，快慢指针，遍历数组，所有结果放在一个列表中，得到最大值

def largestRectangleArea(self, heights: List[int]) -> int:
    if len(heights) == 0:
        return 0
    maxArea = heights[0]
    for i in range(len(heights)):
        minBound = heights[i]
        for j in range(i, len(heights)):
            if heights[j] < minBound:
                minBound = heights[j]
            maxArea = max(maxArea, minBound * (j - i + 1))
    return maxArea

# 写了一版，但是执行超时了，逻辑看了下应该没问题

# 思路2：只遍历一遍柱子，找出每个柱子的左右边界，通过左右边界来确定这
# 个柱子构成的最大面积
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [-1]
    # -1的赋值使得第一个柱子能得到很好的处理
    heights = heights + [0]
    # 这两个初值的处理很巧妙，数组的末尾加一个0，使得不用考虑处理到最
    # 后一个柱子的时候栈不为空的情况，最后一个为0使得栈必定会往前处理
    # 全部弹出
    area = 0
    for i in range(len(heights)):
        if heights[stack[-1]] < heights[i]:
            stack.append(i)
        else:
            while heights[stack[-1]] > heights[i]:
                j = heights[stack.pop()]
                area = max((i - stack[-1] - 1) * j, area)
            stack.append(i)
    return area
# 需要注意的是，栈要用来保存柱子左右边界的下标，方便计算围城的面积