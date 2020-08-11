# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [144]二叉树的后序遍历
@Description :
"""

# 思路1：递归解法，模板需要牢记
def postorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []

    def helper(root):
        if root:
            helper(root.left)
            helper(root.right)
            res.append(root.val)

    helper(root)
    return res

# 执行耗时:64 ms,击败了5.31% 的Python3用户
# 内存消耗:13.6 MB,击败了7.41% 的Python3用户

# 思路2:用递归解法解决
# 解法一、得到中-右-左，然后翻转输出,取巧的做法
def postorderTraversal_iter(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res ,stack = [] , [root]
    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            stack.append(cur.right)
    return res[::-1]

# 执行用时：44 ms, 在所有 Python3 提交中击败了44.20%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了7.41%的用户

# 解法2：按照实际需要的顺序入栈,颜色标记法，给节点加一个标识符，没有遍历过的节点为0，遍历过的为1,1的时候记录节点数据
def postorderTraversal_iter2(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res ,stack = [] , [(0,root)]
    while stack:
        flag ,cur = stack.pop()
        if not cur:
            continue
        if flag == 1:
            res.append(cur.val)
        else:
            stack.append((1 ,cur))
            stack.append((0 ,cur.right))
            stack.append((0 ,cur.left))
    return res

# 执行耗时:52 ms,击败了9.31% 的Python3用户
# 内存消耗:13.7 MB,击败了7.41% 的Python3用户

