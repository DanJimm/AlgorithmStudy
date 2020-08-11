# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/5
@Author      : jim
@File        : [337]打家劫舍Ⅱ
@Description : 
"""

# 思路1：BFS，层序遍历，得到每一层的全部节点，然后隔层相加，看哪种情况的num最大
def rob_BFS(self, root: TreeNode) -> int:
    if not root: return 0
    floor, children, sums = [root], [[root.val]], []
    # 初始化每层需要处理的node，和用来记录每层数据值的list,记录每层总和的sums list
    while floor:
        child = [i for node in floor if node for i in [node.left, node.right]]
        children += [[i.val for i in child if i]]
        floor = [i for i in child if i]
    children.pop()
    for i in range(len(children)):
        sum = 0
        for j in range(len(children[i])):
            sum += children[i][j]
        sums += [sum]
    maxMoney = 0
    for i in range(len(sums)):
        sum = sums[i]
        for k in range(2, len(sums) - i):
            sum = sums[i]
            for j in range(i + k, len(sums), k):
                sum += sums[j]
            maxMoney = max(maxMoney, sum)
        maxMoney = max(maxMoney, sum)
    return maxMoney
# 这个解法有问题，因为相邻层也可能相加

# 改变思路，分别求出当前节点偷与不偷的值,非常优美的分治 递归
def rob_recur(self, root: TreeNode) -> int:
    if not root: return 0
    # 分别返回当前节点偷与不偷，子树的总和
    def calSum(root):
        if not root:
            return [0,0]
        left = calSum(root.left)
        right = calSum(root.right)
        # 不偷当前节点，就返回左和右分别最大的和
        noChoose = max(left[0],left[1]) + max(right[0],right[1])
        # 偷当前节点，就不能偷左和右
        choose = root.val + left[1] + right[1]
        return [choose,noChoose]
    return max(calSum(root)[0],calSum(root)[1])


# 执行耗时: 56ms, 击败了91.63 % 的Python3用户
# 内存消耗: 15.6MB, 击败了85.71 % 的Python3用户
