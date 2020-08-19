# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/16
@Author      : jim
@File        : [127]单词接龙_2
@Description : 
"""

# 二刷单词接龙，首先使用BFS
def ladderLength_BFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    if not endWord in wordList:
        return 0
    queue = [beginWord]
    route, tmp = 1, []

    while queue:
        cur = queue.pop()
        for i in range(len(cur)):
            for j in [chr(k) for k in range(97, 123)]:
                target = cur[:i] + j + cur[i + 1:]
                if target == endWord:
                    route += 1
                    return route
                elif target in wordList:
                    tmp.append(target)
                    wordList.remove(target)
        if len(queue) == 0:
            if len(tmp) == 0:
                return 0
            else:
                queue, tmp = tmp, []
                route += 1
    return route

# 尝试使用双向BFS
def ladderLength_endBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    wordList = set(wordList)
    beginSet = [beginWord]
    endSet = [endWord]

    if not endWord in wordList: return 0

    route, tmp = 1, []
    while beginSet:
        if len(endSet) < len(beginSet):
            beginSet, endSet = endSet, beginSet
        cur = beginSet.pop()
        for i in range(len(cur)):
            for j in [chr(k) for k in range(97, 123)]:
                target = cur[:i] + j + cur[i + 1:]
                if target in endSet:
                    route += 1
                    return route
                elif target in wordList:
                    tmp.append(target)
                    wordList.remove(target)
        if len(beginSet) == 0:
            if len(tmp) == 0:
                return 0
            else:
                beginSet, tmp = tmp, []
                route += 1
    return route


# 执行耗时: 260ms, 击败了41.47 % 的Python3用户
# 内存消耗: 14.4MB, 击败了90.72 % 的Python3用户

# 稍微优化下，就能优化性能，把tmp定义为set类型
# tmp = set([])

# 执行耗时: 152ms, 击败了68.00 % 的Python3用户
# 内存消耗: 14.6MB, 击败了76.38 % 的Python3用户

