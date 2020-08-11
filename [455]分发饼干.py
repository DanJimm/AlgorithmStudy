# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/4
@Author      : jim
@File        : [455]分发饼干
@Description : 
"""

# 思路1、贪心算法，把小孩的胃口和饼干做排序，最大的饼干给胃口大的小孩
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g = sorted(g, reverse=True)
    s = sorted(s, reverse=True)
    if not s: return 0
    num = 0
    while s and g:
        i = s.pop()
        j = g.pop()
        if i >= j:
            num += 1
            continue
        else:
            j = j - i
            while j > 0:
                if not s: break
                i = s.pop()
                j = j - i
            if j > 0 and not s:
                break
            num += 1
    return num
# 解答错误，第19个用例错了一个，问题在于一个孩子只有一个饼干，题看错了，改代码
def findContentChildren_1(self, g: List[int], s: List[int]) -> int:
    g = sorted(g, reverse=True)
    s = sorted(s, reverse=True)
    if not s: return 0
    num = 0
    while s and g:
        i = s.pop()
        j = g.pop()
        if i >= j:
            num += 1
            continue
        else:
            while s:
                i = s.pop()
                if i >= j:
                    num += 1
                    break
    return num

# 执行耗时: 208ms, 击败了64.27 % 的Python3用户
# 内存消耗: 15.5MB, 击败了6.99 % 的Python3用户

# 用双指针再试一下
def findContentChildren_2(self, g: List[int], s: List[int]) -> int:
    g = sorted(g, reverse=True)
    s = sorted(s, reverse=True)
    if not s: return 0
    num = 0
    for i in range(len(g)):
        for j in range(len(s)):
            if s[j] >= g[i]:
                num += 1
                s = s[j + 1:]
                break
            else:
                continue

    return num

# 执行耗时:1648 ms,击败了5.09% 的Python3用户
# 内存消耗:15.4 MB,击败了31.72% 的Python3用户

# 性能有点差，优化一下
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g = sorted(g, reverse=False)
    s = sorted(s, reverse=False)
    if not s: return 0
    g1, s1 = 0, 0
    while s1 < len(s) and g1 < len(g):
        if s[s1] >= g[g1]:
            g1 += 1
        s1 += 1
    return g1

# 执行耗时: 248ms, 击败了20.27 % 的Python3用户
# 内存消耗: 15.3MB, 击败了78.50 % 的Python3用户