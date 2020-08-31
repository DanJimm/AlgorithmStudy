# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/23
@Author      : jim
@File        : [1122]数组的相对排序
@Description : 
"""
# 1.遍历数组，按照数组2的顺序建立一个map分别存储数组1中和数组2一样的元素的个数，数组2中没有的单独记下来排序
# 最后把两个数组结果合并，但是需要额外的空间
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    n2 = len(arr2)
    arr2Map = set(arr2)
    tmp1, tmp2, result = [0] * n2, [], []
    # print(tmp1)
    for i in arr1:
        if not i in arr2Map:
            tmp2.append(i)
        else:
            for j in range(n2):
                if i == arr2[j]:
                    tmp1[j] += 1
    for i in range(n2):
        result += [arr2[i]] * tmp1[i]
    result += sorted(tmp2)
    return result

# 执行耗时: 64ms, 击败了21.37 % 的Python3用户
# 内存消耗: 13.7MB, 击败了55.31 % 的Python3用户

# 2.计数排序，把arr1按照计数排序排出来，然后遍历arr2，输出排序结果，然后把arr2没有的输出
def relativeSortArray_1(self, arr1: List[int], arr2: List[int]) -> List[int]:
    tmp = [0] * 1001
    result = []
    for i in arr1:
        tmp[i] += 1
    for j in range(len(arr2)):
        result += [arr2[j]] * tmp[arr2[j]]
        tmp[arr2[j]] = 0
    for k in range(len(tmp)):
        while tmp[k] != 0:
            result += [k]
            tmp[k] -= 1
    return result

# 执行耗时: 52ms, 击败了64.62 % 的Python3用户
# 内存消耗: 13.6MB, 击败了88.37 % 的Python3用户