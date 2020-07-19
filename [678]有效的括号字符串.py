# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/17
@Author      : jim
@File        : [678]有效的括号字符串
@Description : 
"""

# 思路1：暴力枚举，找到最近的两个成对的括号，并把他们从数组删除，然后循环操作，
# 看最后数组是否为空 时间复杂度O(n^2)
def isValid(self, s: str) -> bool:
    s = list(s)
    map = {'(': ')', '[': ']', '{': '}'}
    i, lenth = 0, len(s)
    if lenth % 2 != 0:
        return False
    while i < lenth:
        if i > lenth // 2 or i == lenth - 1:
            return False
        if s[i] in map:
            if s[i + 1] == map[s[i]]:
                s.pop(i + 1)
                s.pop(i)
                lenth -= 2
                i = 0
                continue
        i += 1
    return True
# 执行结果：
# 通过
# 显示详情
# 执行用时：1816 ms, 在所有 Python3 提交中击败了6.38%的用户
# 内存消耗：
# 13.7 MB, 在所有 Python3 提交中击败了5.22%的用户


# 思路2：用栈解决，遇到一个元素，和前一个元素对比，是成对括号就弹
# 出，否则就压入栈，最后看栈是不是空的 时间复杂度O(n)
def isValid(self, s: str) -> bool:
    s = list(s)
    map = {'(': ')', '[': ']', '{': '}'}
    stack = []
    if  len(s) == 0:
        return True
    for i in s:
        if i in map:
            stack.append(i)
        elif stack == []:
            return False
        else:
            j = stack.pop()
            if i == map[j]:
                continue
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True
# 手写一遍性能提升，但是时间复杂度还是不理想，需要改进
# 执行结果：
# 通过
# 显示详情执行用时：48 ms, 在所有 Python3 提交中击败了33.35%的用户
# 内存消耗：
# 13.6 MB, 在所有 Python3 提交中击败了5.22%的用户

def checkValidString(self, s: str) -> bool:
    s = list(s)
    map = {'(': ')', '[': ']', '{': '}', '?': '?'}
    stack = ['?']
    if len(s) == 0:
        return True
    for i in s:
        if i in map:
            stack.append(i)
        else:
            if i == map[stack.pop()]:
                continue
            else:
                return False
    return len(stack) == 1

# 利用给栈增加一个初始的值，来检验第一个元素为右括号的情况，很
# 巧妙，为空判定的两行代码也可以去掉
# 执行用时：40 ms, 在所有 Python3 提交中击败了77.79%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.22%的用户