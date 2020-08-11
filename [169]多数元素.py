# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/29
@Author      : jim
@File        : [169]多数元素
@Description : 
"""
# 思路1、暴力法，遍历数组，然后记录每个元素的出现频率。然后把map转化为list 排序，输出第一个
def majorityElement(self, nums: List[int]) -> int:
    map = {}
    for i in nums:
        if not i in map:
            map[i] = 1
        else:
            map[i] += 1
    map = sorted(map.items(), key=lambda iterm: iterm[1], reverse=True)
    return map[0][0]

# 时间复杂度O(n)
# 执行耗时: 52ms, 击败了68.42 % 的Python3用户
# 内存消耗: 15.2MB, 击败了6.90 % 的Python3用户

# 思路2：排序法，通过数学分析，数组中的众数会出现在下标n//2的位置
def majorityElement_sort(self, nums: List[int]) -> int:
    nums = sorted(nums)
    return nums[len(nums) // 2]

# 执行耗时: 48ms, 击败了82.68 % 的Python3用户
# 内存消耗: 15MB, 击败了85.71 % 的Python3用户

# 思路3、分治
# 把数组分为左右两部分，众数就在左右两部分各自的众数中产生
def majorityElement_recur(self, nums: List[int]) -> int:
    def helper(l, r):
        # 左右只有一个元素的时候，众数就是自己
        if l == r:
            return nums[l]
        # 分别求出左右两部分的众数
        left = helper(l, (l + r) // 2)
        right = helper((l + r) // 2 + 1, r)

        # 如果两者的众数相等，直接返回
        if left == right:
            return left

        # 统计各自众数出现的次数，次数多的是整体众数
        left_count = sum(1 for i in range(l,r+1) if nums[i] == left)
        right_count = sum(1 for i in range(l,r+1) if nums[i] == right)

        return left if left_count > right_count  else right

    return helper(0, len(nums) - 1)

# 执行耗时:176 ms,击败了5.19% 的Python3用户
# 内存消耗:15.7 MB,击败了5.49% 的Python3用户