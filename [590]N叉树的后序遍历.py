# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [590]N叉树的后序遍历
@Description : 
"""

# 思路1：使用递归模板解答，后序遍历先处理子树，再处理根节点
def postorder_recur(self, root: 'Node') -> List[int]:
    if not root:
        return []
    res = []

    def helper(root):
        if root:
            for child in root.children:
                helper(child)
            res.append(root.val)

    helper(root)
    return res
# 基本的递归代码模板，一定要熟练掌握
# 执行耗时: 68ms, 击败了48.55 % 的Python3用户
# 内存消耗: 15.6MB, 击败了33.33 % 的Python3用户

# 思路2：使用递归算法解决这个问题
def postorder_iter(self, root: 'Node') -> List[int]:
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        stack.extend(cur.children[:])
    return res[::-1]

# 需要注意的是，后序遍历要巧用反序，因为后序遍历的顺序是 子节点1-子节点2-。。-根节点
# 但是栈第一个元素一定是根节点，因此，我们可以先遍历得到，根节点-。。。子节点2-子节点1，然后反向输出，二叉树的后序同理
# 执行耗时: 60ms, 击败了86.27 % 的Python3用户
# 内存消耗: 15.5MB, 击败了33.33 % 的Python3用户