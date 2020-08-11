# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/8
@Author      : jim
@File        : [91]解码方法
@Description : 
"""

# 思路1：类似爬楼梯，可以选择一个一步或者一次两步，但是有一个判断是一次两步需要小于等于26
# 递归求解 注意边界条件
def numDecodings_recur(self, s: str) -> int:
    s, max, result = list(s), len(s), 0

    def helper(level, max, cur):
        nonlocal result
        # terminal
        if level == max:
            result += 1
            return

        # process
        # 处理特殊情况0,分为几种情况，一个0，第二位是0，连续两个0及以上
        if len(cur) == 1 and cur[0] == '0' or len(cur) > 1 and cur[1] == '0' and int(cur[0]) > 2 \
                or len(cur) > 1 and cur[0] == '0':
            result += 0
            return

        # 只取一个数字
        # if len(cur) > 1 and int(cur[1]) != 0:
        helper(level + 1, max, cur[1:])

        # 取两个数字
        if len(cur) >= 2 and int(cur[0]) == 2 and int(cur[1]) <= 6:
            helper(level + 2, max, cur[2:])

        # 取两个数字
        if len(cur) >= 2 and int(cur[0]) == 1:
            helper(level + 2, max, cur[2:])

    helper(0, max, s)
    return result
# 执行会超时

# 思路2：动态规划
# 根据爬楼梯问题延伸，考虑最后一个字符s[i]，如果解码成功
# 1/为s[:i-1]解码，且s[i] != 0
# 2/s[i-1:i+1] 在0-27之间
# 需要考虑的情况有：
# 1、当前可以取一个数字，只要当前节点不为0 都可以取一个数字
# 2、当前可以取两个数字、前一个节点不是0 前一个加当前 < 27
# 3、连续两个0 或者前一个数>=2 直接返回0

def numDecodings_DP1(self, s: str) -> int:
    lenth = len(s)
    if lenth == 0 or s[0] == '0': return 0
    dp = [1, 1]
    for i in range(1, lenth):
        if s[i] == '0' and (s[i - 1] == '0' or int(s[i - 1]) > 2):
            return 0
        elif s[i - 1] == '0' or int(s[i - 1] + s[i]) > 26:
            dp.append(dp[i])
        elif s[i] == '0':
            dp.append(dp[i - 1])
        elif int(s[i - 1] + s[i]) < 27:
            dp.append(dp[i] + dp[i - 1])
    return dp[-1]

# 执行耗时:60 ms,击败了5.35% 的Python3用户
# 内存消耗:13.6 MB,击败了78.92% 的Python3用户
