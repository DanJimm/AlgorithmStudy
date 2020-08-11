# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [589]N叉树的前序遍历
@Description : 
"""

# 思路1：使用递归解法，前序遍历。先访问根节点，然后依次访问每个子节点，以及子节点的子树
def preorder_recur(self, root: 'Node') -> List[int]:
    res = []
    if root == None:
        return []
    def helper(root):
        if (root != None):
            res.append(root.val)
        for child in root.children:
            helper(child)
    helper(root)
    return res

# 最基本的递归模板，前序遍历：先放入根节点，然后调用自身，遍历所有子树
# 执行耗时: 68ms, 击败了50.39 % 的Python3用户
# 内存消耗: 15.8MB, 击败了33.33 % 的Python3用户

# 思路2：使用迭代，手动维护一个栈，依次压入子树节点，然后获取值
def preorder_iter(self, root: 'Node') -> List[int]:
    res = []
    if root == None:
        return []
    stack = [root]
    while stack != []:
        cur = stack.pop()
        res.append(cur.val)
        # for child in cur.children[::-1]:
        #     stack.append(child)
        stack.extend(cur.children[::-1])
    return res

# 简单迭代模板，放入根节点的值之后，栈中压入全部子节点，注意从最后一个开始压，使用extend直接将颠倒后的子节点list加入
# 执行耗时: 60ms, 击败了87.59 % 的Python3用户
# 内存消耗: 15.8MB, 击败了33.33 % 的Python3用户