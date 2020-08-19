# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/12
@Author      : jim
@File        : [208]实现Trie
@Description : 
"""


'''
Trie 的python实现，每一层都是一个{}
    1、初始化的时候，每一层抽象为一个{}，初始化根节点 self.root = {} ,并且当前node初始化一个结束字符'#'
    2、插入操作：首先获取根节点 node = self.root 注意根节点是一个{}
    遍历需要操作的word，每次获得一个字符'S'，查看当前的'S'是否在当前层的{}中
    如果存在，就把node置为'S',继续往下走
    如果不在的话，把这个'S'加入当前层，并且初始化这个'S'为一个{}
    最后一个字符处理完之后，把结束字符加到最后
    3、search操作
    第一步仍然是获取根节点
    遍历word 每一个's' 查看是否在node中，有就继续往下走，没有就返回False
    最后一个字符处理完后，需要check是否有结束字符，如果有返回true,否则说明这只是一个前缀，返回false
    4、start with操作
    基本和search一致，但是走到最后的时候，没有结束字符
 
'''

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        # 根节点初始化为空的{}
        self.end_of_word = "#"
        # 定义一个单词结束的标识


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        # 从根节点开始
        for ch in word:
            # 遍历字符串，下一个节点为当前节点的value
            node = node.setdefault(ch ,{})
        # 最后一个字符加上结束字符
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if not ch in node:
                return False
            node = node[ch]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if not ch in node:
                return False
            node = node[ch]
        return True


# 执行耗时: 136ms, 击败了94.69 % 的Python3用户
# 内存消耗: 26.8MB, 击败了62.31 % 的Python3用户

