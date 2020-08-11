# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/3
@Author      : jim
@File        : [236]二叉树的最近公共祖先
@Description : 
"""
# 思路1：BFS,依次遍历，找到两个目标的祖先列表，然后从后往前找，找到最近的祖先

# 思路2：递归，判断 p q是否在root的左右子树中，方案函数变成一个找p和q的函数，并且看p和q是不是在左右子树中
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q: return root
    # 函数体：在Tree中找到p或者q，就返回找到的值，否则返回None
    left = self.lowestCommonAncestor(root.left, p, q)
    # 在左子树中寻找，找到就返回p或者q，否则返回None
    right = self.lowestCommonAncestor(root.right, p, q)
    # 在右子树中寻找，找到就返回p或者q，否则返回None
    if not left:#左子树中没有p q ，如果右边有，则找到的第一个值就是公共祖先
        return right
    elif not right:#右子树中没有p q ，如果左边有，则找到的第一个值就是公共祖先
        return left
    else:#p和q在root的左右子树中，root是公共祖先
        return root

    # 执行耗时: 88ms, 击败了72.38 % 的Python3用户
    # 内存消耗: 23.7MB, 击败了93.73 % 的Python3用户