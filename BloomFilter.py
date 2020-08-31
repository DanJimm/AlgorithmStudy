# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/21
@Author      : jim
@File        : BloomFilter
@Description : 
"""

from bitarray import bitarray
from mmh3 import mmh3

class BloomFilter:
    def __init__(self,size,hash_num):
        # 初始化传参，分别需要传入二进制列表的大小和hash分布数量两个参数
        self.size = size
        self.hash_num = hash_num
        # 初始化二进制列表
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self,s):
        for seed in range(self.hash_num):
            result = mmh3(seed,s) % self.size
            self.bit_array[result] = 1

    def lookup(self,s):
        for seed in range(self.hash_num):
            if self.bit_array[mmh3(seed,s) % self.size] == 0:return 'Nope'
        return 'Probably'

bf = BloomFilter(10,3)
bf.add('hello')
bf.add('world')
print(bf.lookup('hello'))
print(bf.lookup('bye'))