# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [144]二叉树的前序遍历
@Description : 
"""
# 思路1：递归算法解决，经典模板，需要熟练掌握
def preorderTraversal_recur(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    def helper(root):
        if root:
            res.append(root.val)
            helper(root.left)
            helper(root.right)
    helper(root)
    return res

# 执行耗时: 36ms, 击败了88.26 % 的Python3用户
# 内存消耗: 13.8MB, 击败了7.14 % 的Python3用户

# 改进一下，代码简洁美观
def preorderTraversal_recur2(self, root: TreeNode) -> List[int]:
    def helper(root):
        if not root:
            return []
        return [root.val] + helper(root.left) + helper(root.right)
    return helper(root)
# 执行耗时:40 ms,击败了70.14% 的Python3用户
# 内存消耗:13.7 MB,击败了7.14% 的Python3用户

# 思路2：迭代算法，用栈维护节点列表,也是模板了，需要牢记，不要忘了每次弹出元素的判空
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res , stack = [] , [root]
    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
    return res
# 执行耗时:52 ms,击败了9.85% 的Python3用户
# 内存消耗:13.7 MB,击败了7.14% 的Python3用户