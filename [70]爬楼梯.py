# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/25
@Author      : jim
@File        : [70]爬楼梯
@Description : 
"""

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 思路1：递归，爬楼梯每次只能一级两级，就相当于从下一级跨一步，和从下两级跨两步，问题转化为求f(n-1)+f(n-2)
# 解法1、傻递归
def climbStairs(self, n: int) -> int:
    def helper(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = helper(n - 1) + helper(n - 2)
        return res

    res = helper(n)
    return res
# 时间复杂度太高了，执行会超时

# 解法2、用一个dict缓存中间结果
def climbStairs_dict(self, n: int) -> int:
    if n <= 0:
        return 0
    tmp = {1: 1, 2: 2}

    def helper(n):
        if n in tmp:
            return tmp[n]
        else:
            tmp[n] = helper(n - 1) + helper(n - 2)
        return tmp[n]

    res = helper(n)
    return res

# 执行用时：40 ms, 在所有 Python3 提交中击败了64.72%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了20.59%的用户

# 继续优化，用缓存就不需要helper方法了，直接写list就行：
def climbStairs_list(self, n: int) -> int:
    if n <= 2:
        return n
    tmp = [0] * (n + 1)
    tmp[1], tmp[2] = 1, 2
    for i in range(3, n + 1):
        tmp[i] = tmp[i - 1] + tmp[i - 2]
    return tmp[n]

# 继续优化空间，只保存最后两个值
def climbStairs_final(self, n: int) -> int:
    if n <= 2:
        return n
    a,b = 1,2
    for i in range(3,n+1):
        a , b = b , a+b
    return b

# 执行耗时: 44ms, 击败了38.16 % 的Python3用户
# 内存消耗: 13.7MB, 击败了20.59 % 的Python3用户

# 思路2：从第一级开始爬，每次1或2，直到爬到n
# 不可取，这个和生成括号不一样，生成括号是多结果，这个res是需要累加的

