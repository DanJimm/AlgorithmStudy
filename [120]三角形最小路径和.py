# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/7
@Author      : jim
@File        : [120]三角形最小路径和
@Description : 
"""

# 思路1：DP 转为求 左节点的最小路径和右节点的最小路径中的较小值 + 该节点的值
# 状态数组 f[i][j] = min(f[i+1][j] , f[i+1][j+1]) + t[i][j]
# DP方程，考虑自底向上，从倒数第二层开始往上遍历
# 注意边界条件

def minimumTotal_DP1(self, triangle: List[List[int]]) -> int:
    dict = triangle[:]
    x = len(triangle)
    if x == 0:
        return 0
    elif x == 1:
        return min([triangle[0][i] for i in range(len(triangle[0]))])
    for i in range(x - 2, -1, -1):
        y = len(triangle[i])
        for j in range(y):
            dict[i][j] = min(dict[i + 1][j], dict[i + 1][j + 1]) + triangle[i][j]

    return dict[0][0]

# 用二维数组记录结果，可以优化到用一维数组记录
# 执行耗时:56 ms,击败了28.62% 的Python3用户
# 内存消耗:14.4 MB,击败了32.90% 的Python3用户

# 用一维数组的方式要快很多，感觉挺奇怪的 因为时间复杂度应该都是O(n)
def minimumTotal_DP2(self, triangle: List[List[int]]) -> int:
    x = len(triangle)
    if x == 0:
        return 0
    elif x == 1:
        return min([triangle[0][i] for i in range(len(triangle[0]))])
    list = triangle[-1][:]
    # 初始化list
    for i in range(x - 2, -1, -1):
        y = len(triangle[i])
        tmp = []
        for j in range(y):
            tmp.append(min(list[j], list[j + 1]) + triangle[i][j])
        list = tmp[:]
    return list[-1]

# 执行耗时:44 ms,击败了88.60% 的Python3用户
# 内存消耗:13.9 MB,击败了91.56% 的Python3用户