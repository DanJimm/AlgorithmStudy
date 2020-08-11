# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/23
@Author      : jim
@File        : [11]旋转数组的最小数字
@Description : 
"""
# 思路1：二分查找最小的
# 代码有个问题，当中间的数 和两边的数相等，那么不知道小的值在哪一边
# 这里看了官方的解答，直接把右端点左移一位，这种情况下无法贸然判定
# 只能采用一步一步的方法确定下一个边界
def minArray(self, numbers: List[int]) -> int:
    if not numbers:
        return []
    if numbers[0] < numbers[-1]:
        return numbers[0]
    pre, length = 0, len(numbers) - 1
    while length > pre + 1:
        k = (length - pre) // 2
        if numbers[pre + k] <= numbers[length]:
            length -= k
        elif numbers[pre + k] > numbers[length]:
            pre += k
    return numbers[length]


# 执行耗时: 48ms, 击败了27.67 % 的Python3用户
# 内存消耗: 13.9MB, 击败了100.00 % 的Python3用户