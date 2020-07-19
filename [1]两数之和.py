# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/15
@Author      : jim
@File        : [1]两数之和
@Description : 
"""

# 思路1：暴力枚举 时间复杂度O(n^2)，空间复杂度O(1)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                break
    return result

# 思路2；使用哈希表，保存下访问过的节点和index，每次往哈希表中添加新的元素，都检查一
# 下该值的差值是否存在哈希表中
def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    hashMap = {}
    for index, num in enumerate(nums):
        if target - num in hashMap:
            result.append(hashMap[target - num])
            result.append(index)
        else:
            hashMap[num] = index
    return result

# 优化了一下代码，result数组是不需要的，直接结果拼接输出就可以了
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for index, num in enumerate(nums):
        if target - num in hashMap:
            return [hashMap[target - num]] + [index]
        else:
            hashMap[num] = index

