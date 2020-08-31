# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/24
@Author      : jim
@File        : [493]翻转对
@Description : 
"""
# 1、暴力遍历，双指针遍历，时间复杂度O(n^2)

# 2.归并排序，归并的时候，arr2中的数值比arr1中小，就是一个翻转对
def reversePairs(self, nums: List[int]) -> int:
    result = 0

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        else:
            return merge(mergeSort(arr[:(len(arr) // 2)]), mergeSort(arr[(len(arr) // 2):]))

    def merge(arr1, arr2):
        nonlocal result
        tmp = []
        if len(arr1) == 0 or len(arr2) == 0: return arr1 + arr2
        i = j = 0
        while i < len(arr1) or j < len(arr2):
            if i == len(arr1):
                tmp.append(arr2[j])
                j += 1
            elif j == len(arr2):
                tmp.append(arr1[i])
                i += 1
            elif arr1[i] <= arr2[j]:
                if arr1[i] < 0:
                    for k in range(j, len(arr2)):
                        if arr1[i] / 2 > arr2[k]:
                            result += 1
                tmp.append(arr1[i])
                i += 1
            else:
                for k in range(i, len(arr1)):
                    if arr1[k] / 2 > arr2[j]:
                        result += 1
                tmp.append(arr2[j])
                j += 1
        return tmp

    mergeSort(nums)
    return result
# 执行会超时..

# 修改代码
def reversePairs_0(self, nums: List[int]) -> int:
    def mergesort(nums, begin, end):
        if end <= begin:
            return 0
        mid = (begin + end) // 2
        left = mergesort(nums, begin, mid)
        right = mergesort(nums, mid + 1, end)
        return merge(nums, begin, end) + left + right

    def merge(nums, begin, end):
        ans = 0
        mid = (begin + end) // 2
        i, j = begin, mid + 1
        while i <= mid and j <= end:
            if nums[i] / 2 > nums[j]:
                ans += (mid - i) + 1
                j += 1
            else:
                i += 1
        nums[begin:end + 1] = sorted(nums[begin:end + 1])
        return ans

    return mergesort(nums, 0, len(nums) - 1)

# 执行耗时: 1956ms, 击败了79.91 % 的Python3用户
# 内存消耗: 20.9MB, 击败了28.21 % 的Python3用户

# 再优化一下
def reversePairs_1(self, nums: List[int]) -> int:
    def mergesort(nums, begin, end):
        if end <= begin:
            return 0
        mid = (begin + end) // 2
        left = mergesort(nums,begin,mid)
        right = mergesort(nums,mid+1,end)
        cnt = 0
        i, j = begin, mid + 1
        while i <= mid and j <= end:
            if nums[i] / 2 > nums[j]:
                cnt += (mid - i) + 1
                j += 1
            else:
                i += 1
        nums[begin:end + 1] = sorted(nums[begin:end + 1])
        return cnt + left + right

    return mergesort(nums, 0, len(nums) - 1)

# 执行耗时: 1748ms, 击败了86.23 % 的Python3用户
# 内存消耗: 20.9MB, 击败了38.98 % 的Python3用户

# 比较两种统计cnt的方法，一种超时一种速度较快
def reversePairs_overTime(self, nums: List[int]) -> int:
    def mergesort(nums, begin, end):
        if end <= begin:
            return 0
        mid = (begin + end) // 2
        left = mergesort(nums,begin,mid)
        right = mergesort(nums,mid+1,end)
        cnt = 0
        for i in range(begin, mid + 1):
            for j in range(mid + 1, end + 1):
                if nums[i] / 2 > nums[j]:
                    cnt += (mid - i) + 1
        nums[begin:end + 1] = sorted(nums[begin:end + 1])
        return cnt + left + right

    return mergesort(nums, 0, len(nums) - 1)
