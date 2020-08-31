# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/25
@Author      : jim
@File        : [709]转换成小写字母
@Description : 
"""
# 逻辑简单，主要是大小写操作
def toLowerCase(self, str: str) -> str:
    newStr = ''
    for i in str:
        if 65 <= ord(i) < 91:
            newStr += i.lower()
        else:
            newStr += i
    return newStr

# 执行耗时: 32ms, 击败了95.39 % 的Python3用户
# 内存消耗: 13.8MB, 击败了8.08 % 的Python3用户