# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/22
@Author      : jim
@File        : 排序
@Description : 
"""

arr = [45,23,65,9,24,1,5,62,88,14,3,41,42,33,24]

# 选择排序，依次遍历数组，每次取最小的一个放在最前，总的时间复杂度 O(n^2)

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        smaller ,tmp = arr[i] ,i
        for j in range(i+1,n):
            if smaller > arr[j]:
                tmp = j
                smaller = arr[j]
        arr[i] ,arr[tmp] = arr[tmp] ,arr[i]
    return arr

# 冒泡排序，依次交换相邻两个元素，大的放右边，每次会把当前最大的元素移动到最右，总的时间复杂度 O(n^2)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        k = 0
        for j in range(k+1 ,n-i):
            if arr[k] > arr[j]:
                arr[k] ,arr[j] = arr[j] ,arr[k]
            k += 1
    return arr

# 插入排序,每次把一个元素去和前面已经得到的有序数组比较，插入合适的位置，从1到n，完成排序，时间复杂度O(n^2)
def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] > arr[i]:
                if j==0:
                    arr = [arr[i]] + arr[:i] + arr[i+1:]
                else:
                    arr = arr[:j] + [arr[i]] + arr[j+1:i] + [arr[j]] + arr[i+1:]
    return arr

# 还有一种写法
def InsertionSort_1(arr):
    n = len(arr)
    for i in range(1,n):
        tmp = i
        pre = i-1
        while pre >= 0:
            if arr[pre] > arr[tmp]:
                arr[pre] ,arr[tmp] = arr[tmp] ,arr[pre]
            pre -= 1
            tmp -= 1
    return arr

# 快速排序，分治的思想，每次把比index小的元素放左边，比index大的放右边。然后对左右两个数组递归调用这个方法
# 简单版本的写法,使用额外空间：
def QuickSort(arr):
    def helper(cur):
        index = len(cur) // 2
        if len(cur) <= 1:
            return cur
        left ,right = [], []
        for i in cur:
            if i < cur[index]:
                left.append(i)
            elif i != cur[index]:right.append(i)
        return helper(left) + [cur[index]] + helper(right)
    return  helper(arr)

# 更好的写法可以不用额外的空间
def QuickSort_NoRoom(arr, begin, end):

    def patition(arr, begin , end):
        pivot, j = end , begin
        for i in range(begin, pivot):
            if arr[i] < arr[pivot]:
                arr[i] ,arr[j] = arr[j] ,arr[i]
                j += 1
        arr[j], arr[pivot] = arr[pivot], arr[j]
        pivot = j
        return pivot

    if begin >= end:
        return

    pivot = patition(arr, begin, end)
    QuickSort(arr, begin, pivot-1)
    QuickSort(arr, pivot+1, end)
    return arr



# 归并排序，类似快排，先把数组一分为二，然后分别排序子数组，最后合起来
def mergeSort(arr):
    def merge(left, right):
        '''
        merge 方法实现输入两个有序数组，将他们合并为一个有序数组
        :param left:
        :param right:
        :return: 返回整体有序数组
        '''
        l, r = len(left), len(right)
        result = []
        i = j = 0
        while i < l or j < r:
            if i == l:
                result.append(right[j])
                j += 1
            elif j == r:
                result.append(left[i])
                i += 1
            elif left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j +=1
        return result
    if len(arr) < 2:return arr

    return merge(mergeSort(arr[:len(arr)//2]),mergeSort(arr[len(arr)//2:]))