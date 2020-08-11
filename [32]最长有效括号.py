# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/10
@Author      : jim
@File        : [32]最长有效括号
@Description : 
"""

# 思路1：暴力法，快慢指针找出所有有效括号，然后找出最长的一个

# 思路2：DP
# 1、子问题
# 如果一个括号字符串是有效的括号，那么再加长变为有效括号，则需要再增加一个‘（’ 和 一个‘）’

# 2、状态定义
# dp[i][j] 表示 [i] - [j]之间是有效的括号
# if dp[i+1][j-1] == 1 and s[j] == ')' or dp[i][j-2] == 1 and s[j-1]=='(' s[j] == ')'

# 3、状态转移方程
#
#尝试解法1：
def longestValidParentheses_DP1(self, s: str) -> int:
    l = len(s)
    if l <= 1: return 0
    dp = [[0 for _ in range(l)] for _ in range(l)]
    pareList, finalDict, longest = {}, {}, 0

    for i in range(l - 2, -1, -1):
        for j in range(i + 1, l):
            if i == j - 1:
                dp[i][j] = 1 if s[i] == '(' and s[j] == ')' else 0
            elif dp[i + 1][j - 1] == 1 and s[i] == '(' and s[j] == ')' or \
                    dp[i][j - 2] == 1 and s[j - 1] == '(' and s[j] == ')':
                dp[i][j] = 1
            else:
                dp[i][j] = 0
            if dp[i][j] == 1: pareList[i] = (j - i + 1)
    for i in pareList:
        while i + pareList[i] < l:
            if (i + pareList[i]) in pareList:
                pareList[i] = pareList[i] + pareList[(i + pareList[i])]
            else:
                break
        longest = max(longest, pareList[i])
    return longest

# 解答失败：
# 114 / 230

# 学习官方题解
# 1、子问题
# 如果一个括号字符串是有效的括号，末尾是 ）

# 2、状态定义
# dp[i]表示以下标为 i的前面所有的，括号最长的长度
# 如果 s[i-1] = ( s[i] = ) dp[i] = dp[i-2] + 2
# 如果 s[i-1] = ) s[i] = ) 则前面需要找到和 s[i-1] 匹配 （
# 匹配的位置是 ：
#          i=  0  1  2  3 4  5  6  7
#             （  ） （ （ （  ） ） ）
#                    |  |_______|  i
#                    |   dp[i]=4
#                    i-dp[i]-1
#          dp  1  2  3  4 5  6  7  8
#
# 3、状态转移方程
def longestValidParentheses_DP2(self, s: str) -> int:
    l = len(s)
    if l <= 1: return 0
    dp, maxLen = [0 for _ in range(l + 1)], 0
    for i in range(1, l):
        if s[i] == '(':
            dp[i + 1] = 0
        elif s[i - 1] == '(':
            dp[i + 1] = dp[i - 1] + 2
        elif s[i - 1] == ')':
            if i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == '(':
                dp[i + 1] = dp[i] + 2 + dp[i - dp[i] - 1]
            else:
                dp[i + 1] = 0
        maxLen = max(maxLen, dp[i + 1])
    return maxLen


# 执行耗时:72 ms,击败了17.03% 的Python3用户
# 内存消耗:13.8 MB,击败了60.43% 的Python3用户

# 思路2：用栈解决
# 自己尝试了一下：
def longestValidParentheses(s):
    l = len(s)
    if l <= 1:return 0
    stack ,longest = [] , 0
    left ,right = -1,-1
    for i in range(l):
        if stack == []:
            if s[i] == '(':
                stack.append(s[i])
                if left == -1:left = i
            elif s[i] == ')':left = -1
        elif stack != []:
            if s[i] == '(':stack.append(s[i])
            else:
                stack.pop()
                if not stack:
                    right = i
                    longest = max(longest, (right - left + 1))
    return longest
# 这个思路不行，只能判断从起始位置开始的合理括号

# 参考官方题解，用栈维护元素下标，且栈顶元素为最后一个没有匹配的’）‘，这样可以保证当前栈里的尾减去栈顶的下标
# 就是有效括号的长度
def longestValidParentheses_stack1(self, s: str) -> int:
    l = len(s)
    if l <= 1: return 0
    stack, longest = [-1], 0
    for i in range(l):
        # 遇到左括号就入栈，或者栈空的时候入栈第一个右括号
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            elif stack:
                longest = max(longest, (i - stack[-1]))
    return longest

# 代码类似判断字符串是否为有效括号，注意需要放一个占位元素，防止数组越界
# 执行耗时: 56ms, 击败了71.12 % 的Python3用户
# 内存消耗: 14.2MB, 击败了35.25 % 的Python3用户
