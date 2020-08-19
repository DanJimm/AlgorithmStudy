# -*- coding: utf-8 -*-

"""
@Time        : 2020/8/18
@Author      : jim
@File        : [322]零钱兑换
@Description : 
"""
# 思路1：BFS，不断的用amount减去硬币的面额，直到减到0，返回level
def coinChange_BFS(self, coins: List[int], amount: int) -> int:
    if amount == 0: return 0

    coins = sorted(coins,reverse=True)
    queue = deque()
    queue.append(amount)
    level = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            for coin in coins:
                next = cur - coin
                if next == 0:
                    return level + 1
                elif next > 0:
                    queue.append(next)
        level += 1
    return -1

# 尝试加了贪心的思想，还是超时了..

# 思路2：DFS，遍历分支，然后求出所有分支的最短
def coinChange_DFS(self, coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    if len(coins) == 0: return -1

    coins = sorted(coins, reverse=True)
    result = float("inf")

    def dfs(next, level):
        if next < 0: return
        nonlocal result
        for coin in coins:
            if coin == next:
                result = min(result, level)
                return
            dfs(next - coin, level + 1)

    dfs(amount, 1)
    return result if result != float("inf") else -1
# 还是会超时。。。

# 优化傻递归，增加记忆化搜索，自顶向下
def coinChange_DFS1(self, coins: List[int], amount: int) -> int:
    dict = {0: 0}
    for coin in coins:
        dict[coin] = 1

    def find(num):
        if num in dict:
            return dict[num]
        pre = [(num - coin) for coin in coins if coin <= num]
        if len(pre) >= 1:
            dict[num] = min([find(num - coin) for coin in coins if coin <= num]) + 1
            return dict[num]
        else:
            return float("inf")

    result = find(amount)
    return result if result != float("inf") else -1

# 终于过了、、、
# 执行耗时: 2392ms, 击败了7.52 % 的Python3用户
# 内存消耗: 29.6MB, 击败了13.85 % 的Python3用户

# 试试自底向上
def coinChange_DFS2(self, coins: List[int], amount: int) -> int:
    if coins == [0] and amount != 0: return -1
    dict = {0: 0}
    for coin in coins:
        dict[coin] = 1
    minCoin = min(coins)

    num = 0
    while num <= amount:
        if 0 < num < minCoin:
            dict[num] = float("inf")
        elif not num in dict:
            dict[num] = min([dict[num - coin] for coin in coins if coin <= num]) + 1
        num += 1

    result = dict[amount]
    return result if result != float("inf") else -1

# 没想到性能提升这么大、、
# 执行耗时: 1168ms, 击败了89.56 % 的Python3用户
# 内存消耗: 14.5MB, 击败了19.75 % 的Python3用户

#思路3：DP
# DP[i] 为金额为i的时候，最小的兑换步数
# DP[i] = min( DP[i-coin] ) + 1,其实和上面的自底向上思路是一样的，看看能否进一步优化