# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/2
@Author      : jim
@File        : [55]跳跃游戏
@Description : 
"""

# 思路1：贪心算法，从后往前找能到最后一格子的最前的格子
def canJump_1(self, nums: List[int]) -> bool:
    reachNode = len(nums) - 1
    for i in range(reachNode - 1, -1, -1):
        if nums[i] >= reachNode - i:
            reachNode = i
    if reachNode == 0:
        return True
    else:
        return False

# 执行耗时:40 ms,击败了97.69% 的Python3用户
# 内存消耗:15 MB,击败了71.86% 的Python3用户

# 普通思路是从第一个格子往后看，用一个list维护当前能到达的格子，
# 然后从这个list的依次取出一个格子循环，直到所有格子处理完，看能不能到达最后的一个格子





