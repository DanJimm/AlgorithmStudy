# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [541]反转字符串Ⅱ
@Description : 
"""
# 分治，每个2k的段做一次翻转
def reverseStr(self, s: str, k: int) -> str:
    def reverse(s, k):
        if len(s) >= k:
            tmp = list(s[:k])
        else:
            tmp = list(s)
        i, j = 0, len(tmp) - 1
        while i < j:
            tmp[i], tmp[j] = tmp[j], tmp[i]
            i += 1
            j -= 1
        ans = ''
        for i in tmp:
            ans += i
        return ans + s[k:] if len(s) >= k else ans

    if len(s) <= 1: return s
    l = len(s) // (2 * k)
    result = ''
    if l >= 1:
        for i in range(l):
            result += reverse(s[i * 2 * k:(i + 1) * 2 * k], k)
        return result + reverse(s[l * 2 * k:], k)
    else:
        return reverse(s, k)

# 执行耗时: 40ms, 击败了79.54 % 的Python3用户
# 内存消耗: 13.6MB, 击败了90.14 % 的Python3用户