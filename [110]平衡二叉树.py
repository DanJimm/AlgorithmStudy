# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/17
@Author      : jim
@File        : [110]平衡二叉树
@Description : 
"""

# 思路1：DFS，分别求左右子树的深度,并且判断到当前节点为止，是否为平衡
def isBalanced_DFS1(self, root: TreeNode) -> bool:
    def dfs(root):
        if not root:
            return (0, True)

        elif root.left and root.right:
            leftNode = dfs(root.left)
            rightNode = dfs(root.right)
            level = max(leftNode[0] + 1, rightNode[0] + 1)
            return (level, abs(leftNode[0] - rightNode[0]) <= 1 and leftNode[1] and rightNode[1])

        elif not root.left and not root.right:
            return (1, True)

        elif not root.right:
            leftNode = dfs(root.left)
            return (leftNode[0] + 1, leftNode[0] < 2)

        elif not root.left:
            rightNode = dfs(root.right)
            return (rightNode[0] + 1, rightNode[0] < 2)

    return dfs(root)[1]

# 执行耗时: 64ms, 击败了73.59 % 的Python3用户
# 内存消耗: 18.6MB, 击败了15.36 % 的Python3用户

# 可以优化下，遇到非平衡就不用继续判断了
def isBalanced_DFS2(self, root: TreeNode) -> bool:
    flag = True

    def dfs(root):
        nonlocal flag
        if not root:
            return (0 , True)
        if flag == False:
            return (0,False)

        elif root.left and root.right:
            leftNode = dfs(root.left)
            rightNode = dfs(root.right)
            level = max(leftNode[0]+1,rightNode[0]+1)
            flag = abs(leftNode[0] - rightNode[0]) <= 1 and leftNode[1] and rightNode[1]
            return (level, flag)

        elif not root.left and not root.right:
            return (1, True)

        elif not root.right:
            leftNode = dfs(root.left)
            flag = leftNode[0] < 2
            return (leftNode[0]+1,flag)

        elif not root.left:
            rightNode = dfs(root.right)
            flag = rightNode[0] < 2
            return (rightNode[0]+1,flag)

    return dfs(root)[1]
# 执行用时：56 ms, 在所有 Python3 提交中击败了92.70%的用户
# 内存消耗：18.6 MB, 在所有 Python3 提交中击败了14.24%的用户