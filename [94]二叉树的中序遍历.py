# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [94]二叉树的中序遍历
@Description : 
"""

# 思路1：标准递归解法模板,必须牢记
def inorderTraversal_recur(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []

    def helper(root):
        if root:
            helper(root.left)
            res.append(root.val)
            helper(root.right)

    helper(root)
    return res
# 执行耗时:32 ms,击败了96.27% 的Python3用户
# 内存消耗:13.6 MB,击败了7.84% 的Python3用户

# 递归解法的代码可以改进下，但是影响执行效率
def inorderTraversal_recur2(self, root: TreeNode) -> List[int]:
    def helper(root):
        if not root:
            return []
        return helper(root.left) + [root.val] + helper(root.right)
    return helper(root)

# 执行耗时:44 ms,击败了43.93% 的Python3用户
# 内存消耗:13.7 MB,击败了7.84% 的Python3用户

# 思路2：迭代解法，手动维护栈，按照顺序压入节点，中序遍历需要注意，栈的流程为：
# 根入栈-左子树入栈-左子树出栈-根出栈-右子树入栈-右子树出栈
# 出栈的时候获取值，实现中序遍历
# 这个是模板，需要牢记
def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    stack ,res ,cur= [] , [] ,root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        res.append(tmp.val)
        cur = tmp.right
    return res

# 执行耗时: 48ms, 击败了18.50 % 的Python3用户
# 内存消耗: 13.7MB, 击败了7.84 % 的Python3用户
