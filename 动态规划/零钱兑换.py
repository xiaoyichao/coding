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
    def coinChange(self, coins: List[int], amount: int) -> int: # dp 数组的迭代解法 labuladong解法
        dp = [amount +1] * (amount+1) # 其实float('inf') 换成amount+1 也可以，因为最大能取到amount，因为有根节点的存在，所以是amount+1长度的列表
        # 比如要组成11个的硬币数值，你最差的情况是用11个1元的硬币，你从根节点需要一直往下走11层，加上根节点，既是11+1=12层。
        # base case
        dp[0] = 0
        for i in range(amount+1): #for 循环在遍历所有状态的所有取值，这两层可以调换，
            for coin in coins: #for 循环在求所有选择的最小值
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])

        return -1 if dp[amount]==amount +1 else dp[amount]

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