# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/24
@Author      : jim
@File        : [264]丑数2
@Description : 
"""
# 官方题解，用一个队来保存待处理的丑数，然后通过已有的丑数，推导后续衍生的新数
# 这里用到了一个思想：两级优化，将算出来的丑数预存在一个list，后续只需要从这个list里面取出来就行

from heapq import *

class Ugly:
    def __init__(self):
        self.nums = nums = []
        # 存储所有的丑数
        ugly = {1, }
        # 记录已经出现过的丑数
        heap = []
        # 用一个堆来存放待处理的丑数
        heappush(heap, 1)
        # 推入第一个丑数：1

    # 每次弹出小根堆中最小的一个，得到由他散发的三个丑数，判断是否出现过
        for i in range(1690):
            tmp = heappop(heap)
            nums.append(tmp)
            for j in [2, 3, 5]:
                num = tmp * j
                if not num in ugly:
                    heappush(heap, num)
                    ugly.add(num)


class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n-1]

# 执行耗时:52 ms,击败了88.81% 的Python3用户
# 内存消耗:13.8 MB,击败了12.50% 的Python3用户