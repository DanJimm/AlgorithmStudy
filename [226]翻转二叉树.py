# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/25
@Author      : jim
@File        : [226]翻转二叉树
@Description : 
"""
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:


# 思路1：递归,DFS遍历树，交换节点的左右子树
def invertTree_recur(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    def exchange(root):
        if not root:
            return
        if root:
            root.left, root.right = root.right, root.left
            exchange(root.left)
            exchange(root.right)

    exchange(root)
    return root

# 执行耗时: 40ms, 击败了71.22 % 的Python3用户
# 内存消耗: 13.7MB, 击败了5.26 % 的Python3用户

# 优化代码，其实不需要额外的exchange方法，调用自身就可以了
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None
    if root:
        root.left , root.right = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
    return root
# 但是时间复杂度比较差
# 执行耗时: 48ms, 击败了20.06 % 的Python3用户
# 内存消耗: 13.8MB, 击败了5.26 % 的Python3用户

# 思路2：BFS迭代解决
def invertTree_iter(self, root: TreeNode) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            stack.append(cur.left)
            stack.append(cur.right)
            cur.left , cur.right = cur.right , cur.left
    return root

# 执行耗时: 36ms, 击败了88.12 % 的Python3用户
# 内存消耗: 13.6MB, 击败了5.26 % 的Python3用户