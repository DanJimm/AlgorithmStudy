# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/22
@Author      : jim
@File        : [429]N叉树的层序遍历
@Description : 
"""
# 思路1：递归解决
def levelOrder_recur(self, root: 'Node') -> List[List[int]]:
    floor, res = [root], []
    def helper(floor):
        child, value = [], []
        if floor != [None]:
            for i in floor:
                value.append(i.val)
                if i.children:
                    child.extend(i.children)
                else:
                    continue
            if value:
                res.append(value)
            if child:
                helper(child)
        return res
    return helper(floor)

# 思路是用一个helper ，传入一层节点的list 然后把这层的值传入，并返回下一层的list
# 执行用时：68 ms, 在所有 Python3 提交中击败了54.55%的用户
# 内存消耗：15.7 MB, 在所有 Python3 提交中击败了50.00%的用户

# 思路2：广度优先遍历，一层一层的遍历N叉树，不重新定义helper
def levelOrder(self, root: 'Node') -> List[List[int]]:
    floor , res = [root] , []
    if root is None:
        return []
    while floor:
        res.append([i.val for i in floor])
        floor = [child for node in floor for child in node.children]
    return res
# 使用更优雅的代码实现，背下来这个代码模板
# 执行用时：64 ms, 在所有 Python3 提交中击败了75.09%的用户
# 内存消耗：15.7 MB, 在所有 Python3 提交中击败了50.00%的用户