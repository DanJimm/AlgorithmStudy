# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/2
@Author      : jim
@File        : [860]柠檬水找零
@Description : 
"""

# 思路1：获取一个需要找零列表，然后和收入列表去匹配
def lemonadeChange(bills):
    # 待找零的金额
    pay = sorted([i - 5 for i in bills if i != 5], reverse=False)
    # 可以用的零钱
    money = sorted([i for i in bills if i != 20], reverse=False)

    while pay:
        cur = pay.pop()
        if len(money) == 0:
            return False
        for j in range(len(money)-1,-1,-1):
            if cur >= money[j]:
                cur = cur - money[j]
                money.pop(j)
                if cur == 0:
                    break
    return True
# 错误解法，需要按照账单顺序来处理，不能全部获取后再处理

# 修改代码：
def lemonadeChange(self, bills: List[int]) -> bool:

    if bills[0] != 5: return False

    money = []
    for i in bills:
        if i == 5:
            money.append(i)
        elif len(money) == 0:
            return False
        else:
            m = i - 5
            # 需要找零的钱
            money = sorted(money)
            while m != 0:
                if len(money) == 0:
                    return False

                for j in range(len(money) - 1, -1, -1):
                    if m == 0:
                        break
                    elif m < money[0]:
                        # print('剩下的钱不能找零')
                        return False
                    elif m >= money[j]:
                        m -= money[j]
                        money.pop(j)

            if i == 10:
                money.append(i)
    return True

# 效率不高
# 执行用时：496 ms, 在所有 Python3 提交中击败了5.05%的用户
# 内存消耗：13.9 MB, 在所有 Python3 提交中击败了38.36%的用户

# 使用贪心算法解决：维护5 和 10 的列表
def lemonadeChange_3(self, bills: List[int]) -> bool:
    ten = five =0
    if bills[0] != 5:return False
    for i in bills:
        if i == 5:five += 1
        elif i == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:return False
        elif i == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five > 3:
                five -= 3
            else:return False

    return True
# 执行用时：228 ms, 在所有 Python3 提交中击败了11.46%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了67.12%的用户

# 再优化一下判断：
def lemonadeChange_4(self, bills: List[int]) -> bool:
    ten = five =0
    if bills[0] != 5:return False
    for i in bills:
        if i == 5:five += 1
        elif i == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:return False
        elif i == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five > 3:
                five -= 3
            else:return False
    return True

# 执行用时：168 ms, 在所有 Python3 提交中击败了86.54%的用户
# 内存消耗：14 MB, 在所有 Python3 提交中击败了5.48%的用户