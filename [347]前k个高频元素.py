# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/23
@Author      : jim
@File        : [347]前k个高频元素
@Description : 
"""
# 思路1：使用堆解决，将元素和频率对应入堆，最后依次返回频率高的元素
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) * k == 0:
        return []
    count, hotCount, res = Counter(nums), [], []
    for i in count.keys():
        heappush(hotCount, (-count[i], i))
    for i in range(k):
        tmp = heappop(hotCount)
        res.append(tmp[1])
    return res

# 先获取元素和频率的哈希表，按照频率的顺序入堆，需要注意的是，python的堆是小根堆，所以要获取最大频率，要翻转入堆
# 执行耗时: 60ms, 击败了38.16 % 的Python3用户
# 内存消耗: 16.7MB, 击败了100.00 % 的Python3用户

# 通过学习实例代码，可以在获取count后进行一下排序，然后输出heapq的前n值实现
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) * k == 0:
        return []
    count, res = Counter(nums), []
    res = sorted(count.items(), key=lambda iterm: iterm[1], reverse=True)
    # 将字典按照频率值，由大到小排序
    return list(map(lambda iterm: iterm[0], res))[:k]
    # 将排序后的数组，只取第一个值出来，取前k个

# 执行耗时:44 ms,击败了94.38% 的Python3用户
# 内存消耗:16.7 MB,击败了100.00% 的Python3用户