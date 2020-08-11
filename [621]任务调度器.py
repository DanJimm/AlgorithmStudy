# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/9
@Author      : jim
@File        : [621]任务调度器
@Description : 
"""

# 贪心，先安排次数最多的任务，每一个任务后面有n个空格，最后两种情况，一种是空格可以放下其余的任务
# 1、空格多于不同的任务数，任务填不满所有空格：result = (max_num-1)*(n+1) + num(出现次数最多的元素的数量)
# 2.空格很少，不够所有任务填，所有任务依次执行

def leastInterval(self, tasks: List[str], n: int) -> int:
    map = Counter(tasks)
    wordList = map.most_common()
    # 按照任务出现的次数排序
    same_max = [i for i in map if map[i] == wordList[0][1]]
    return max((wordList[0][1] - 1) * (n + 1) + len(same_max), len(tasks))


# 执行耗时: 60ms, 击败了91.89 % 的Python3用户
# 内存消耗: 13.9MB, 击败了73.26 % 的Python3用户
