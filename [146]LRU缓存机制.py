# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/22
@Author      : jim
@File        : [146]LRU缓存机制
@Description : 
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.remain = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        result = self.dict.pop(key)
        self.dict[key] = result
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:self.dict.popitem(last = False)
        self.dict[key] = value