# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/16
@Author      : jim
@File        : [126]单词接龙Ⅱ
@Description : 
"""

# 思路：同单词接龙1，BFS，只不过需要记录所有遍历过的单词还有前后关系，
# 有个想法，用一个字典保存，例如 relation = { word1 : (x ,y)},其中x ,y分别为前序和下一个节点，
# 再用一个dict保存每一层的单词 floor = {1:[word1 ,word2 ...]}
# BFS遍历的时候，判断每一层单词的关联单词是否在wordlist ，并且是否已经被记录过了,如果没有记录过
# 就吧word加入relation 和 floor ，并且把它的后序单词加入tmp

def findLadders(beginWord, endWord, wordList):
    # 把wordlist变成字典，方便后序的查询
    if not endWord in wordList:return []
    wordList.append(beginWord)
    wordList = set(wordList)
    l = len(beginWord)

    # 尝试用桶的思想来处理，提升查询性能，具体的方式是把每个单词的所有可能的变换保存在dict，
    # 提升查询速度
    wordBuck = {}
    for word in wordList:
        for i in range(l):
            mark = word[:i] + '*' + word[i + 1:]
            if not mark in wordBuck:
                wordBuck[mark] = [word]
            else:wordBuck[mark].append(word)

    #BFS
    relation ,wordLevel ,tmp ,level = {beginWord:([],[])} ,{0:[beginWord]} ,set([]) ,1
    curWord ,tmp ,flag = [beginWord] ,set([]) ,False

    while curWord:
        cur = curWord.pop()
        for i in range(l):
            mark = cur[:i] + '*' + cur[i + 1:]
            curWordList = wordBuck[mark]
            wordBuck[mark].remove(cur)
            # 得到i位置的相关单词列表
            for next in curWordList:
                # 如果遇到终点，则标记True，这一层走完就跳出循环
                if next == endWord: flag = True
                if not next in relation:
                    #第一次遇到该单词
                    relation[next] = ([cur],[])
                    relation[cur][1].append(next)
                    wordLevel.setdefault(level,[]).append(next)
                    tmp.add(next)
                else:
                    relation[next][0].append(cur)
                    relation[cur][1].append(next)

        # 这一层走完了
        if len(curWord) == 0:
            if flag == True:break
            elif len(tmp) == 0:
                return []
            else:
                level += 1
                curWord , tmp = list(tmp) , set([])

    # 处理得到的list，拼接成需要的结果
    floor = len(wordLevel)
    result = []
    def dfs(floor,tmp,preWord):
        if floor == 0:
            tmp.append(wordLevel[0][0])
            tmp.reverse()
            nonlocal result
            result.append(tmp)
            return
        for i in wordLevel[floor]:
            if i in relation[preWord][0]:
                dfs(floor-1,tmp+[i],i)

    dfs(floor-2,[endWord],endWord)

    return result


# 执行耗时: 168ms, 击败了62.87 % 的Python3用户
# 内存消耗: 20.6MB, 击败了11.50 % 的Python3用户

# 优化一下：
def findLadders_BFS2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    # 把wordlist变成字典，方便后序的查询
    if not endWord in wordList: return []
    wordList.append(beginWord)
    wordList = set(wordList)
    l = len(beginWord)

    # 尝试用桶的思想来处理，提升查询性能，具体的方式是把每个单词的所有可能的变换保存在dict，
    # 提升查询速度
    wordBuck = {}
    for word in wordList:
        for i in range(l):
            mark = word[:i] + '*' + word[i + 1:]
            if not mark in wordBuck:
                wordBuck[mark] = [word]
            else:
                wordBuck[mark].append(word)

    # BFS
    relation, wordLevel, level = {beginWord: ([])}, {0: [beginWord]}, 1
    curWord, tmp, flag = [beginWord], set([]), False

    while curWord:
        cur = curWord.pop()
        for i in range(l):
            mark = cur[:i] + '*' + cur[i + 1:]
            curWordList = wordBuck[mark]
            wordBuck[mark].remove(cur)
            # 得到i位置的相关单词列表
            for next in curWordList:
                # 如果遇到终点，则标记True，这一层走完就跳出循环
                if next == endWord: flag = True
                if not next in relation:
                    # 第一次遇到该单词
                    relation[next] = ([cur])
                    wordLevel.setdefault(level, []).append(next)
                    tmp.add(next)
                else:
                    relation[next].append(cur)

        # 这一层走完了
        if len(curWord) == 0:
            if flag == True:
                break
            elif len(tmp) == 0:
                return []
            else:
                level += 1
                curWord, tmp = list(tmp), set([])

    # 处理得到的list，拼接成需要的结果
    floor = len(wordLevel)
    result = []

    def dfs(floor, tmp, preWord):
        if floor == 0:
            tmp.append(wordLevel[0][0])
            tmp.reverse()
            nonlocal result
            result.append(tmp)
            return
        for i in wordLevel[floor]:
            if i in relation[preWord]:
                dfs(floor - 1, tmp + [i], i)

    dfs(floor - 2, [endWord], endWord)

    return result

# 优化了一下空间，之前存了不需要的内容
# 执行耗时: 160ms, 击败了64.58 % 的Python3用户
# 内存消耗: 19.1MB, 击败了21.24 % 的Python3用户

# 还可以进一步优化，可以使用双向BFS