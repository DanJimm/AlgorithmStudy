# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/23
@Author      : jim
@File        : [153]寻找旋转排序数组中的最小值
@Description : 
"""
# 思路1：二分查找 注意，这里基于旋转数组的特点，只需要比较中值和最右侧的大小即可确定收缩方向
def findMin(self, nums: List[int]) -> int:
    if not nums:
        return []
    if nums[0] < nums[-1]:
        return nums[0]
    pre, length = 0, len(nums) - 1
    while length > pre + 1:
        k = (length - pre) // 2
        if nums[pre + k] < nums[length]:
            length -= k
        elif nums[pre + k] > nums[length]:
            pre += k
    return nums[length]

# 执行耗时: 44ms, 击败了45.87 % 的Python3用户
# 内存消耗: 13.9MB, 击败了6.67 % 的Python3用户
