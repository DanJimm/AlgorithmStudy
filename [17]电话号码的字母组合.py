# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/30
@Author      : jim
@File        : [17]电话号码的字母组合
@Description : 
"""

#回溯的思想解决，每次尝试往位置里放一个值，然后传到下一层的函数处理
def letterCombinations(self, digits: str) -> List[str]:
    def getValue(num):
        digits = {}
        digits['2'] = 'abc'
        digits['3'] = 'def'
        digits['4'] = 'ghi'
        digits['5'] = 'jkl'
        digits['6'] = 'mno'
        digits['7'] = 'pqrs'
        digits['8'] = 'tuv'
        digits['9'] = 'wxyz'
        return digits[num]

    if len(digits) == 0: return []

    def helper(level, Max, tmp, res):
        # terminal 走到最后一层就返回结果
        if level == Max:
            res.append(tmp)
            return

        # process
        for i in getValue(digits[level]):
            # drill down
            helper(level + 1, Max, tmp + i, res)

        # clean status
        return res

    return helper(0, len(digits), '', [])

# 执行耗时: 36ms, 击败了86.42 % 的Python3用户
# 内存消耗: 13.8MB, 击败了19.28 % 的Python3用户
