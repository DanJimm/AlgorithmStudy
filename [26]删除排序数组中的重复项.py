# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/15
@Author      : jim
@File        : [26]删除排序数组中的重复项
@Description : 
"""

# 思路1：暴力遍历，双指针，第一个每次遇到不同的
# 元素后，停止，另一个指针往前走，如果元素相同，就删除，时间复杂度O(n^2)
def removeDuplicates(self, nums: List[int]) -> int:
    i, lengh = 0, len(nums)
    while i < lengh - 1:
        for j in range(i + 1, lengh):
            if nums[i] == nums[j]:
                nums.pop(j)
                j += 1
                lengh -= 1
                break
            else:
                i += 1
    return lengh
# 最终结果：
# 执行用时：64 ms
# 内存消耗：14.8 MB

#思路2：根据官方题解启发，不用考虑非重复新数组部分后面的情况，那么可以直接把遇到
# 的不同元素的值赋给慢指针的位置，可以对思路1进行改进
def removeDuplicates_exchange(self, nums: List[int]) -> int:
    if nums == []:
        return 0
    i, newlen = 0, 1
    for j in range(i + 1, len(nums)):
        if nums[j] == nums[i]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
            j += 1
            newlen += 1
    return newlen
# 最终结果：
# 执行耗时: 44ms, 击败了89.03 % 的Python3用户
# 内存消耗: 14.6MB, 击败了8.16 % 的Python3用户
