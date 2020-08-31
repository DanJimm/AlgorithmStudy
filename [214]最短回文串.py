# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/29
@Author      : jim
@File        : [214]最短回文串
@Description : 
"""
'''
1/添加字符能形成回文串，需要先找字符串原先就有的回文部分，然后依次在字符串前加上后序不是回文的部分
'''


def shortestPalindrome(self, s: str) -> str:
    n = len(s)
    if n <= 1: return s

    def isPal(s):
        l = len(s)
        a, b = 0, l - 1
        while a <= b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True

    if isPal(s): return s

    l = 0
    for i in range(1, n):
        if isPal(s[:i + 1]):
            l = i

    return s[-1:l:-1] + s
#运行超时，看看怎么优化一下

# 最简洁的解法O(n)，找最长公共前缀
def shortestPalindrome_1(self, s: str) -> str:
    rev = s[::-1]
    n = len(s)
    for i in range(n + 1):
        if s.startswith(rev[i:]):
            return rev[:i] + s
    return s

# 执行耗时: 76ms, 击败了73.77 % 的Python3用户
# 内存消耗: 13.8MB, 击败了78.71 % 的Python3用户