# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-09 16:53:58
LastEditTime: 2023-01-09 18:36:02
Description: https://leetcode.cn/problems/coin-change/
'''
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # 递归
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = float('inf')
        for coin in coins:
            sub_problem =  self.dp(coins, amount-coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return -1 if res==float('inf') else res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # 带备忘录的递归
        self.mem = {}
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if amount in self.mem.keys():
            return self.mem[amount]
            
        res = float('inf')
        for coin in coins:
            sub_problem =  self.dp(coins, amount-coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        self.mem[amount] =  -1 if res==float('inf') else res
        return self.mem[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # dp 数组的迭代解法 labuladong解法
        dp = [float('inf')] * (amount+1) # 其实float('inf') 换成amount+1 也可以，因为最大能取到amount
        # base case
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])

        return -1 if dp[amount]==float('inf') else dp[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # dp 数组的迭代解法 官方解法
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
