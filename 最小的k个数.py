# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/23
@Author      : jim
@File        : 最小的k个数
@Description : 
"""
# 思路1：排序，然后输出结果
def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    temp = sorted(arr)
    res = [temp[i] for i in range(k)]
    return res
# 还可以改进下，代码更美观


# 执行耗时:60 ms,击败了88.11% 的Python3用户
# 内存消耗:14.8 MB,击败了100.00% 的Python3用户

# 思路2：用最小堆实现，吧所有元素入堆，然后依次弹出k次
def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    arrNew, res = [], []
    for i in arr:
        heappush(arrNew, i)
    for i in range(k):
        res.append(heappop(arrNew))
    return res

# 执行耗时:72 ms,击败了61.86% 的Python3用户
# 内存消耗:14.6 MB,击败了100.00% 的Python3用户

# 优化堆的实现，不用全部插入堆中，因为要求最小k，所以维护一个最大堆，依次往后遍历，如果新元素小于max，
# 就弹出根新元素入堆,这样全部遍历之后，得到的就是最小的k个值
def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    arrNew = [-x for x in arr[:k]]
    heapq.heapify(arrNew)
    for i in arr[k:]:
        if -i > arrNew[0]:
            heapq.heapreplace(arrNew,-i)
    res = [-i for i in arrNew]
    return res

# 执行耗时: 60ms, 击败了88.11 % 的Python3用户
# 内存消耗: 15.2MB, 击败了100.00 % 的Python3用户
