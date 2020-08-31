# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/29
@Author      : jim
@File        : [206]反转链表
@Description : 
"""

'''
1/哨兵节点，递归反转链表
'''
def reverseList(self, head: ListNode) -> ListNode:
    if not head: return head
    pre = None
    while head.next:
        p = head.next
        head.next = pre
        pre = head
        head = p
    head.next = pre
    return head

# 执行耗时: 52ms, 击败了29.86 % 的Python3用户
# 内存消耗: 14.7MB, 击败了43.75 % 的Python3用户

'''
2/尝试一下递归的方法
'''

def reverseList_recur(self, head: ListNode) -> ListNode:
    if not head: return head

    def helper(node, pre):
        if not node.next:
            node.next = pre
            return node
        p = node.next
        node.next = pre
        return helper(p, node)

    return helper(head, None)

# 执行耗时: 44ms, 击败了77.03 % 的Python3用户
# 内存消耗: 19.6MB, 击败了5.09 % 的Python3用户
