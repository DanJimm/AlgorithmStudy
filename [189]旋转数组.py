# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/17
@Author      : jim
@File        : [189]旋转数组
@Description : 
"""

# 思路1：拓展数组空间K，用来存放后k个元素，然后前面元素后移k，
# 再把原先的后k个元素放在开头，删除最后k个元素，结果是错的,没有考虑k超过长度的情况
def rotate(self, nums: List[int], k: int) -> None:
    length = len(nums)
    nums = nums + [0] * k
    m = -1
    for i in range(length - 1, -k - 1, -1):
        nums[m] = nums[i]
        m -= 1
    for j in range(-k, 0):
        nums.pop(j)

# 思路2：直接使用python的切片拼接,空间复杂度不符合，结果也是错的,没有考虑k超过长度的情况
def rotate(self, nums: List[int], k: int) -> None:
    k = k % length
    # 需要增加这一行处理k超长的情况
    nums = nums[(len(nums)-k):] + nums[:(len(nums)-k-1)]

# 思路3：官方题解，三次反转 分别旋转数组的两部分
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    k = k % length
    # 处理k的原因，是因为k可能超过数组长度
    def swap(l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    swap(0, length - k - 1)
    swap(length - k, length - 1)
    swap(0, length - 1)


# 解答成功:
# 执行耗时: 36ms, 击败了94.24 % 的Python3用户
# 内存消耗: 14MB, 击败了59.46 % 的Python3用户


# 思路4：移动数组k次 时间复杂度很差
def rotate(self, nums: List[int], k: int) -> None:
    while k > 0:
        p = nums[-1]
        nums.pop(-1)
        nums.insert(0, p)
        k -= 1


# 解答成功:
# 执行耗时: 128ms, 击败了18.19 % 的Python3用户
# 内存消耗: 13.9MB, 击败了91.89 % 的Python3用户
