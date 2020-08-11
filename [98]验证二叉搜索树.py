# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/26
@Author      : jim
@File        : [98]验证二叉搜索树
@Description : 
"""
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 思路1：利用二叉搜索树的定义，用中序遍历，判断是否是有序结果
# DFS:得到遍历结果，然后判断是否是有序的
def isValidBST_recur(self, root: TreeNode) -> bool:
    if not root:
        return True
    res = []

    def dfs(root):
        if not root:
            return
        if root:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
    dfs(root)
    return sorted(res) == res and len(res) == len(set(res))

# 执行耗时: 60ms, 击败了53.26 % 的Python3用户
# 内存消耗: 17.4MB, 击败了9.52 % 的Python3用户

# 优化代码，用一个pre记录上一个最小值，直接在每次执行结果的时候就判断是否满足大小关系
def isValidBST_recur2(self, root: TreeNode) -> bool:
    if not root:
        return True
    self.pre = float('-inf')

    def dfs(root):
        if not root:
            return True
        if root:
            if not dfs(root.left):
                return False
            if root.val > self.pre:
                self.pre = root.val
            else:
                return False
            return dfs(root.right)
    return dfs(root)

# 执行耗时: 56ms, 击败了74.28 % 的Python3用户
# 内存消耗: 16.7MB, 击败了9.52 % 的Python3用户

# BFS:迭代解决中序遍历一定要注意入栈和出栈顺序
def isValidBST_iter1(self, root: TreeNode) -> bool:
    if not root:
        return True
    stack ,cur ,res= [] , root, []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        res.append(tmp.val)
        cur = tmp.right
    print(res)
    return sorted(res) == res and len(res) == len(set(res))

# 执行耗时:56 ms,击败了74.28% 的Python3用户
# 内存消耗:16.6 MB,击败了9.52% 的Python3用户

# 优化代码，实时比较
def isValidBST_iter2(self, root: TreeNode) -> bool:
    if not root:
        return True
    stack ,cur ,pre= [] ,root, float('-inf')
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        if tmp.val <= pre:
            return False
        pre = tmp.val
        cur = tmp.right
    return True

# 执行耗时: 48ms, 击败了96.54 % 的Python3用户
# 内存消耗: 16.1MB, 击败了9.52 % 的Python3用户

# 思路3、DFS上下界比较法
def isValidBST(self, root: TreeNode) -> bool:
    if not root:
        return True
    front, post=  float('-inf') , float('inf')
    def isBST(root ,front ,post ):
        if not root:
            return True
        if root:
            if root.val <= front or root.val >= post:
                return False
        return isBST(root.left, front, root.val) and isBST(root.right, root.val , post)
        #判断两条分支，都为true才是二叉搜索树

    return isBST(root,front,post)

# 执行耗时:56 ms,击败了74.28% 的Python3用户
# 内存消耗:16 MB,击败了9.52% 的Python3用户