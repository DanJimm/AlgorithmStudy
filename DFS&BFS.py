# -*- coding: utf-8 -*-

"""
@Time        : 2020/7/24
@Author      : jim
@File        : DFS&BFS
@Description : 
"""

# DFS 迭代
# 记录遍历过的节点

def DFS(node,visited):
    # 终止条件，全部节点都访问完了一遍
    if node in visited:
        return

    visited.add(node)
    # 将访问过的节点加入数组保存--重要

    # 继续处理下一层的节点
    for node_next in node.child:
        if not node_next in visited:
            DFS(node_next,visited)


# BFS队列维护一个待访问的节点列表
def BFS(gragh,start,stop):
    queue = []
    queue.append(start)

    visited = set()

    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        # 处理当前节点
        nodes = gragh_related_nodes(node)
        # 找到关联的其他节点，并将其他节点推入队列
        queue.push(nodes)



