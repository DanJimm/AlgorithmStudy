# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/27
@Author      : jim
@File        : [78]子集
@Description : 
"""
# 思路1、回溯的思想，对每个位置的元素进行判断，选择添加或者不添加

def subsets_recur(self, nums: List[int]) -> List[List[int]]:
    res, n = [], len(nums)
    # 定义新的方法，每次传入当前已有的结果，和走到的位置，判断当前位置是都放入这个位置的元素
    def setValue(m, tmp, res):
        # terminal
        if m == n:
            res.append(tmp)
            return

        # process_2 不添1加当前节点
        setValue(m + 1, tmp, res)

        # process_1 添加当前的节点
        setValue(m + 1, tmp + [nums[m]], res)

        # clear status

    setValue(0, [], res)
    return res
# 执行耗时: 40ms, 击败了73.03 % 的Python3用户
# 内存消耗: 13.9MB, 击败了5.72 % 的Python3用户

# 代码改进，每次看一个元素，往已有结果中添加，多次联系，做到能默写代码
def subsets_recur2(self, nums: List[int]) -> List[List[int]]:
    result, n = [], len(nums)
    #生成每一层的子集，然后遍历后序的元素，往前面的结果添加，不断的产生新的分支，
    # 每一个分支都是在前一个结果上加上当前元素
    def helper(i, tmp):
        result.append(tmp)
        for j in range(i, n):
            helper(j + 1, tmp + [nums[j]])
    helper(0, [])
    return result

# 执行耗时: 36ms, 击败了89.53 % 的Python3用户
# 内存消耗: 13.9MB, 击败了5.72 % 的Python3用户


# 迭代的思想，每一轮操作后，结果保存，然后往结果中添加新元素，非常优秀的代码
def subsets_iter(self, nums: List[int]) -> List[List[int]]:
    result = [[]]
    for num in nums:
        result += [res + [num] for res in result]
    return result

# 执行耗时:44 ms,击败了48.77% 的Python3用户
# 内存消耗:13.6 MB,击败了5.72% 的Python3用户



