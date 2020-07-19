# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/14
@Author      : jim
@File        : tesrCode
@Description : 
"""

height = [1,1]

def largestRectangleArea(heights):
    stack = [-1]
    heights = heights + [0]
    area = 0
    for i in range(len(heights)):
        print('i is ',i,'height[i] is',heights[i])
        print('stack is ',stack)
        if heights[stack[-1]] < heights[i]:
            stack.append(i)
            print('stack is ',stack)
        else:
            while heights[stack[-1]] > heights[i]:
                j = heights[stack.pop()]
                print('j is ',j)
                area = max((i-stack[-1]-1)*j,area)
                print('area is ',area)
            stack.append(i)
    return area

print(largestRectangleArea(height))