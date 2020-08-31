# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/28
@Author      : jim
@File        : [5]最长回文子串
@Description : 
"""

'''
1/动态规划解决
定义状态dp[i][j] == 1,表示i-j之间是回文子串
if dp[i+1][j-1] == 1 and s[j] == s[i]:
    dp[i][j] == 1
else
    dp[i][j] == 0
    
'''


def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n <= 1: return s
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    tmp, dict = 1, {}
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if j == i:
                dp[i][j] = 1
                tmp = max(tmp, (j - i + 1))
                dict.setdefault((j - i + 1), []).append((i, j))
            elif j == i + 1 and s[i] == s[j]:
                dp[i][j] = 1
                tmp = max(tmp, (j - i + 1))
                dict.setdefault((j - i + 1), []).append((i, j))
            elif dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                dp[i][j] = 1
                tmp = max(tmp, (j - i + 1))
                dict.setdefault((j - i + 1), []).append((i, j))

    result = ''
    for i in range(dict[tmp][0][0], dict[tmp][0][1] + 1):
        result += s[i]
    return result

# 执行用时：7936 ms, 在所有 Python3 提交中击败了5.00%的用户
# 内存消耗：73.3 MB, 在所有 Python3 提交中击败了5.11%的用户

# 优化一下
def longestPalindrome_1(self, s: str) -> str:
    n = len(s)
    if n <= 1: return s
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    tmp, ans = 1, (0, 0)
    for i in range(n - 1, -1, -1):
        for j in range(i+1, n):
            if j == i:
                dp[i][j] = 1
                if j - i + 1 > tmp:
                    tmp = j - i + 1
                    ans = (i, j)
            elif j == i + 1 and s[i] == s[j]:
                dp[i][j] = 1
                if j - i + 1 > tmp:
                    tmp = j - i + 1
                    ans = (i, j)
            elif dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                dp[i][j] = 1
                if j - i + 1 > tmp:
                    tmp = j - i + 1
                    ans = (i, j)
    return s[ans[0]:ans[1] + 1]

# 执行用时：4640 ms, 在所有 Python3 提交中击败了39.35%的用户
# 内存消耗：22.4 MB, 在所有 Python3 提交中击败了5.11%的用户

'''
尝试一下中心扩展法
'''

def longestPalindrome_2(self, s: str) -> str:
    n = len(s)
    if n <= 1: return s
    l, result = 0, (0, 0)
    # 先扩散元素
    for i in range(n):
        a, b = i - 1, i + 1
        while 0 <= a < n and 0 <= b < n:
            if s[a] == s[b]:
                tmp = b - a + 1
                if tmp > l:
                    l = tmp
                    result = (a, b)
                a -= 1
                b += 1
            else:
                break
    # 再扩散中间节点
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            if l < 2:
                l = 2
                result = (i, i + 1)
            a, b = i - 1, i + 2
            while 0 <= a < n and 0 <= b < n:
                if s[a] == s[b]:
                    tmp = b - a + 1
                    if tmp > l:
                        l = tmp
                        result = (a, b)
                    a -= 1
                    b += 1
                else:
                    break
        else:
            continue

    return s[result[0]:result[1] + 1]

# 执行耗时: 1596ms, 击败了65.21 % 的Python3用户
# 内存消耗: 13.8MB, 击败了57.35 % 的Python3用户