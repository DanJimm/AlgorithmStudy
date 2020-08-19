# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/12
@Author      : jim
@File        : [212]单词搜索Ⅱ
@Description : 
"""

# 使用Trie解决

# 实现字典树
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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
    if len(words) == 0: return []
    row, col, l = len(board), len(board[0]), len(words)
    if row == 0: return []

    n = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    # 把board转换成一个Trie
    Trie1 = Trie()
    result = []

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

    for word in words:
        if Trie1.search(word): result.append(word)

    return result

# 执行超时了，进一步优化思路
# 思维的方向错了，应该是先把words存入Trie,然后在board中找

def findWords_Trie2(self, board: List[List[str]], words: List[str]) -> List[str]:

    # 判断边界条件
    if len(words) == 0: return []
    row, col, l = len(board), len(board[0]), len(words)
    if row == 0: return []

    # 构造字典树
    Trie = {}
    for word in words:
        node = Trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = '#'

    result = []
    n = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def getWord(x, y, visited, word1, CurTrie):
        ch = board[x][y]
        if ch in CurTrie:
            if '#' in CurTrie[ch]:
                if not word1 + ch in result:result.append(word1+ch)
            list = [(x + x1, y + y1) for (x1, y1) in n
                    if 0 <= x + x1 < row if 0 <= y + y1 < col
                    if not (x + x1, y + y1) in visited]
            for i in list:
                x1, y1 = i
                getWord(x1, y1, visited + [(x, y)], word1 + ch, CurTrie[ch])
        else:
            return

    for node in [(x, y) for x in range(row) for y in range(col)]:
        x, y = node
        getWord(x, y, [(x, y)], '', Trie)

    return result

# 执行耗时: 448ms, 击败了16.10 % 的Python3用户
# 内存消耗: 28.2MB, 击败了42.78 % 的Python3用户

def findWords_Trie3(self, board: List[List[str]], words: List[str]) -> List[str]:

    # 定义以及实现字典树
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = 'end'

    # 定义dfs的方法
    def dfs(x, y, curTrie, s):
        ch = board[x][y]
        if ch in curTrie:
            # 找到一个单词
            if '#' in curTrie[ch] and not s + ch in result:
                result.append(s + ch)
            # 走过的暂时置为@，以免走重了
            board[x][y] = '@'
            # ch在trie中，可以进入下一层
            for i in [(x + x1, y + y1) for x1, y1 in n
                      if 0 <= x + x1 < row if 0 <= y + y1 < col
                      if board[x + x1][y + y1] != '@']:
                x2, y2 = i
                dfs(x2, y2, curTrie[ch], s + ch)
            board[x][y] = ch
            # 记得把值改回来
        else:
            return

    row, col = len(board), len(board[0])
    n = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []
    # 定义处理程序
    for i in range(row):
        for j in range(col):
            dfs(i, j, trie, '')

    return result

# 执行耗时: 408ms, 击败了20.53 % 的Python3用户
# 内存消耗: 28.1MB, 击败了68.12 % 的Python3用户