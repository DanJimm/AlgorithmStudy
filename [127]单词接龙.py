# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/1
@Author      : jim
@File        : [127]单词接龙
@Description : 
"""

# 思路1：BFS，依次遍历wordlist，获取可以得到end的路径，把wordlist转化成一个有向图
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    num, origin = 1, [beginWord]

    def compare(str1, str2):
        num = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                num += 1
        if num > 1: return False
        return True

    if not endWord in wordList:
        return 0
    elif compare(beginWord, endWord):
        return 2

    while wordList:
        flag, tmp = False, []
        for i in origin:
            for j in wordList:
                if compare(i, j):
                    flag = True
                    tmp.append(j)
        num += 1
        if flag == False: return 0
        origin = [] + tmp
        wordList = [i for i in wordList if i not in origin]
        for l in origin:
            if compare(l, endWord):
                num += 1
                return num
# 超时了

# 疯狂优化一下计算量;
def ladderLength_BFS1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    num, origin = 1, [beginWord]
    if beginWord in wordList: wordList.remove(beginWord)

    def compare(str1, str2):
        num = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                num += 1
        if num > 1: return False
        return True

    if not endWord in wordList:
        return 0
    elif compare(beginWord, endWord):
        return 2

    while wordList:
        flag, tmp = False, []
        for i in origin:
            for j in wordList[:]:
                if compare(i, j):
                    flag = True
                    tmp.append(j)
                    wordList.remove(j)

        num += 1
        if flag == False: return 0
        origin = [] + tmp
        if endWord in origin:
            return num

# 36 / 43 个通过测试用例 个通过测试用例 然后超时了。。。实际本地执行了一下还是挺快的。。。

#采用字母遍历获得相关单词列表的思路，尝试写了一下，终于通过了
def ladderLength_BFS_letter(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    if not endWord in wordList:return 0
    if beginWord in wordList:wordList.remove(beginWord)

    word_dic ,relation ,visited= set(wordList) ,{} ,{}
    num ,flag = 1 ,False
    queue = [beginWord]

    def let_origin(str):
        # 建立关系字典
        if not str in relation:
            relation[str] = []
        for m in range(len(str)):
            list_str = list(str)
            for i in [chr(j) for j in range(97, 123)]:
                list_str[m] = i
                tmp = ''.join(list_str)
                if tmp in word_dic and tmp != str and not tmp in relation[str] :
                    if tmp == endWord:
                        return True
                    else:relation[str] = relation[str] + [tmp]

    while queue:
        tmp_list ,cur_list = [] ,[]
        for cur in queue:
            visited[cur] = 'True'
            cur_list.append(cur)
            if let_origin(cur):
                num += 1
                return num
        for word in cur_list:
            for i in relation[word]:
                if not i in visited:
                    tmp_list.append(i)
        queue = [] + tmp_list
        num += 1

    if flag == False:num = 0
    return num

# 执行用时：2668 ms, 在所有 Python3 提交中击败了8.29%的用户
# 内存消耗：16.6 MB, 在所有 Python3 提交中击败了52.04%的用户

# 还可以改进一下，主要改动每层循环体
# while queue:
#     tmp_list = []
#     for cur in queue:
#         visited[cur] = 'True'
#         print('cur is',cur)
#         if let_origin(cur):
#             num += 1
#             return num
#         for i in relation[cur]:
#             if not i in visited:
#                 tmp_list.append(i)
#     queue = [] + list(set(tmp_list))
#     print('queue is',queue)
#     num += 1
#     print('num is',num)

# 执行用时：964 ms, 在所有 Python3 提交中击败了12.66%的用户
# 内存消耗：16.6 MB, 在所有 Python3 提交中击败了52.04%的用户