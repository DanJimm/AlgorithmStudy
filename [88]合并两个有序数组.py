# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/16
@Author      : jim
@File        : [88]合并两个有序数组
@Description : 
"""

# 思路1：创建一个新数组，遍历两个目标数组，分别将头元素放进数组，不满足原地操作的要求

# 思路2：直接合并数组，然后排序，这个时间复杂度太高了

# 思路3：官方题解，从后方开始遍历，一次把较大元素放到nums1的结尾
# 自己看了题解写了一版代码，效率不好，感觉逻辑也有冗余
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if nums1 == [] or nums2 == []:
        return nums1
    i, j, index = m - 1, n - 1, m + n - 1
    while index >= 0 and j >= 0:
        if i < 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1
            continue
        if nums1[i] > nums2[j]:
            nums1[index], nums1[i] = nums1[i], nums1[index]
            i -= 1
        else:
            nums1[index] = nums2[j]
            j -= 1
        index -= 1
    return nums1


# 解答成功:
# 执行耗时: 48ms, 击败了23.66 % 的Python3用户
# 内存消耗: 13.6MB, 击败了6.90 % 的Python3用户

# 看一下官方的代码，优化逻辑判断
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if nums1 == [] or nums2 == []:
        return nums1
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[i + j + 1] = nums1[i]
            i -= 1
        else:
            nums1[i + j + 1] = nums2[j]
            j -= 1
    while i < 0 and j >= 0:
        nums1[i + j + 1] = nums2[i + j + 1]
        j -= 1
    return nums1


# 解答成功:
# 执行耗时: 36ms, 击败了89.79 % 的Python3用户
# 内存消耗: 13.6MB, 击败了6.90 % 的Python3用户