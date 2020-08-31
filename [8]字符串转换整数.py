# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [8]字符串转换整数
@Description : 
"""
# 挨个判断字符
def myAtoi(self, str: str) -> int:
    if len(str) == 0: return 0
    result = ''
    sign = ''
    flag_F, flag_N = False, False
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    f = ['+', '-']
    for i in str:
        if (flag_N == True or flag_F == True) and not i in num:
            break
        elif flag_N == False and not i in f and not i in num and i != ' ':
            return 0
        elif i in f and flag_F == False:
            sign += i
            flag_F = True
        elif i in num:
            result += i
            flag_N = True
    if result == '': return 0
    if sign == '-':
        return max((-1) * int(result), (-2 ** 31))
    else:
        return min(int(result), (2 ** 31 - 1))

# 执行耗时: 36ms, 击败了97.38 % 的Python3用户
# 内存消耗: 13.7MB, 击败了43.51 % 的Python3用户