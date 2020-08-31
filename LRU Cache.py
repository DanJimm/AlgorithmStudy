# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/21
@Author      : jim
@File        : LRU Cache
@Description : 
"""

# LRU Cache
'''
主要实现的功能为，根据出现的频率进行元素的排序和增加删除，最近使用的元素总是排在最前，并且按照频率排序，
当size不够的时候，频率最低的元素优先被删除
'''

from collections import OrderedDict

class LRUCache(object):
    def __init__(self,capacity):
        # 初始化存储字典
        self.dict = OrderedDict()
        # remain是最大存储长度
        self.remain = capacity

    def get(self, key):
        if not key in self.dict:
            return -1
        # 把对应的值取出来，然后还需要存回dict开头
        result = self.dict.pop(key)
        self.dict[key] = result
        return result

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                # 先弹出最早添加的元素，然后再加入
                self.dict.popitem(last=False)
        self.dict[key] = value