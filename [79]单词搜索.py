# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/12
@Author      : jim
@File        : [79]单词搜索
@Description : 
"""

# 思路1：遍历搜索，图的DFS遍历，回溯
def exist_DFS(self, board: List[List[str]], word: str) -> bool:
    if len(word) == 0: return True
    row, col, n = len(board), len(board[0]), len(word)
    if row == 0: return False

    word = list(word)
    nextNode = [(x, y) for x in range(row) for y in range(col) if board[x][y] == word[0]]
    if n == 1:
        if len(nextNode) >= 1:
            return True
        else:
            return False

    visited, flag = [], False

    def findNext(index, x, y, visited):
        # 在(x, y)附近找是否存在目标节点，存在就返回坐标
        tmp = []
        n = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        list = [(x + x1, y + y1) for (x1, y1) in n
                if 0 <= x + x1 < row if 0 <= y + y1 < col
                if not (x + x1, y + y1) in visited]
        for (x2, y2) in list:
            if board[x2][y2] == word[index]:
                tmp += [(x2, y2)]
        return tmp if tmp != [] else False

    def helper(index, x, y, visited):
        # terminal
        nonlocal flag
        if flag: return

        if index == n:
            flag = True
            return

        # process
        tmp = findNext(index, x, y, visited)

        # drill down
        if tmp != False:
            for node in tmp:
                x1, y1 = node
                helper(index + 1, x1, y1, visited + [(x1, y1)])
        elif tmp == False:
            return

    for i in nextNode:
        x, y = i
        helper(1, x, y, visited + [(x, y)])

    return flag
# 写的有点繁琐了，还有优化的空间
# 执行耗时: 432ms, 击败了8.47 % 的Python3用户
# 内存消耗: 18.2MB, 击败了5.01 % 的Python3用户

# 思路2：用Trie，把board转换为一个Trie,然后看word在不在Trie
def exist(self, board: List[List[str]], word: str) -> bool:

    class Trie(object):
        def __init__(self):
            self.root = {}
            self.end_of_word = '#'

        def insert(self, word):
            node = self.root
            for ch in word:
                node = node.setdefault(ch, {})
            node[self.end_of_word] = self.end_of_word

        def search(self, word):
            node = self.root
            for ch in word:
                if ch in node:
                    node = node[ch]
                else:
                    return False
            return True
            # if not self.end_of_word in node:return False


    # 判断边界条件
    if len(word) == 0: return True
    row, col, l = len(board), len(board[0]), len(word)
    if row == 0: return False

    nextNode = [board[x][y] for x in range(row) for y in range(col)]
    if l == 1:
        if word in nextNode:
            return True
        else:
            return False

    n = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    # 把board转换成一个Trie
    Trie1 = Trie()

    def getWord(x, y, visited, word1):
        list = [(x + x1, y + y1) for (x1, y1) in n
                if 0 <= x + x1 < row if 0 <= y + y1 < col
                if not (x + x1, y + y1) in visited]
        if list == []:
            Trie1.insert(word1)
            return
        for i in list:
            x1, y1 = i
            getWord(x1, y1, visited + [(x1, y1)], word1 + board[x1][y1])

    for node in [(x, y) for x in range(row) for y in range(col)]:
        x, y = node
        getWord(x, y, [(x, y)], '' + board[x][y])

    return Trie1.search(word)
# 超时了，调整思路

# 把word放进Trie
def exist_Trie2(self, board: List[List[str]], word: str) -> bool:

    # 判断边界条件
    if len(word) == 0: return True
    row, col, l = len(board), len(board[0]), len(word)
    if row == 0: return False

    # 把 word 转换成一个Trie
    trie = {}
    node = trie
    for ch in word:
        node = node.setdefault(ch, {})
    node["#"] = '#'

    flag = False

    def getWord(x, y, visited, curTrie):

        ch = board[x][y]

        if ch in curTrie:
            # 找到一个字符，进入下一层
            if '#' in curTrie[ch]:
                nonlocal flag
                flag = True
                return
            list = [(x + x1, y + y1) for (x1, y1) in n
                    if 0 <= x + x1 < row if 0 <= y + y1 < col
                    if not (x + x1, y + y1) in visited]
            for i in list:
                x1, y1 = i
                getWord(x1, y1, visited + [(x, y)], curTrie[ch])
        else:
            return

    n = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for node in [(x, y) for x in range(row) for y in range(col)]:
        x, y = node
        getWord(x, y, [], trie)

    return flag
