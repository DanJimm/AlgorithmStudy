# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/18
@Author      : jim
@File        : [155]最小栈
@Description : 
"""
# 思路：
# 因为需要有O(1)时间复杂度返回最小元素的要求。因此需要一个辅助栈，minStack
# 来保存当前元素中的最小值，同时维护一个数据栈dataStack保存全部元素

def __init__(self):

    self.dataStack = []
    self.minStack = [math.inf]
    # 很巧妙的使用负无穷占位，避免了数组越界和没有元素的时候，getmin的问题

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        self.minStack.append(min(x, self.minStack[-1]))
        # 保证每次push元素，data和min都会同步增加一样的长度，这样pop的
        # 时候，两个栈一起删除栈顶的元素就可以了


    def pop(self) -> None:
        self.dataStack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.dataStack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]