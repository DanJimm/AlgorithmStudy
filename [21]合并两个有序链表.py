# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/16
@Author      : jim
@File        : [21]合并两个有序链表
@Description : 
"""

# 思路1：挨个遍历，两个指针在两个链表移动，如果链表2的元素大于链表一，就插入相应位置
# 试了下，不好实现，因为判断数量可能很多，判断完头结点的值，判断的位置还会后移，导致
# 最后需要判断很多才能知道插入位置

# 思路2：官方解法-递归 不停的判断两个链表的头结点数值,把问题递归成最小集：判断两个节点
# 的大小，较小的节点指向较大的节点。最初的问题的每一步就是判断两个头结点，较小的节点
# 指向其余节点的合集，时间复杂度O(m+n) 空间复杂度O(1)
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
        # 返回l1，是因为这里用l1的头结点指向其他节点的合集，因此最后剩下的是l1链表
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        # 返回l2，是因为这里用l2的头结点指向其他节点的合集，因此最后剩下的是l2链表

# 最终结果：
# 执行用时：
# 64 ms, 在所有 Python3 提交中击败了7.59%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了7.14%的用户



# 思路3：是否可以用哈希，先全部遍历一遍？存下每个节点和他next的对应关系，然后按照
# 大小插入相应的位置？

# 思路4：官方题解 迭代，用一个哨兵指针来新建一个链表，用指针pre记录每一次比较两个
# 链表头结点的较小值 时间复杂度O(m+n) 空间复杂度，只有一个哨兵节点O(m+n)
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    prehead = ListNode(-1)
    pre = prehead
    while l1 and l2:
        if l1.val < l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next
    pre.next = l1 or l2
    return prehead.next
# 结果：
# 解答成功:
# 执行耗时: 44ms, 击败了81.61 % 的Python3用户
# 内存消耗: 13.6MB, 击败了7.14 % 的Python3用户