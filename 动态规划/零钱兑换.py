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
    def coinChange(self, coins: List[int], amount: int) -> int: # 递归 会超时的哦
        return self.dp(coins, amount)
    
    def dp(self, coins, amount):
        # base case
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = amount +1
        for coin in coins:
            sub_problem =  self.dp(coins, amount-coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return -1 if res==amount +1 else res


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # 带备忘录的递归,这个时间复杂度是O(n)，不会超时
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
            
        res = amount +1 # 最差的情况就是全是1的硬币组成的结果，所以amount +1 肯定取不到，当然，可以用float('inf')
        for coin in coins:
            sub_problem =  self.dp(coins, amount-coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        self.mem[amount] =  -1 if res==amount +1 else res
        return self.mem[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化一个长度为 amount+1 的数组，用 amount+1 来表示不可达
        dp  = [amount+1]*(amount+1)
        # base case，凑成总金额为 0 的硬币数为 0
        dp[0] = 0
        
        # 遍历硬币数组中的每一个硬币
        for coin in coins:
            # 遍历总金额范围，从 coin 到 amount
            for i in range(coin, amount+1):
                # 如果当前金额 i 减去当前硬币的面值 coin 小于 0，说明当前硬币不能选，直接跳过
                # 否则，当前金额 i 可以由 dp[i-coin] 转移过来，选取当前硬币 coin 需要花费 1，因此加 1
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        # 返回凑成总金额 amount 的最少硬币数，如果凑不出，返回 -1
        return dp[amount] if dp[amount]!=amount+1 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # dp 数组的迭代解法 官方解法
        dp = [amount +1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != amount +1 else -1 


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)
    def dp(self, coins, amount):
        if amount==0:
            return 0
        if amount <0:
            return -1
        res = amount +1
        for coin in coins:
            sub_problem = self.dp(coins, amount-coin)
            if sub_problem ==-1:
                continue
            res= min(res, sub_problem+1)
        return -1 if res==amount +1 else res
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]* (amount+1)
        
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
                
        return -1 if dp[amount]==amount+1 else dp[amount]


s = Solution()
res = s.coinChange([1,2,5], 11)
print(res)