"https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/"
from typing import List


class Solution:
    # dp 全记录版本
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n)]
        for i in range(n):
            if i == 0:  # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]  # 买入的话，利润就是-prices[i]
            else:
                # 状态转移方程
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)  # 卖出的过程减费用的话，只需要在这个位置操作，要是买入的时候减手续费，第一天的位置也得操作，因为第一天也可以买入，但是第一天不能卖出。
        return dp[n-1][0]   

    # 只记录最近的两种情况的版本
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1, n, 1):
            dp_0 = max(dp_0, dp_1+prices[i]-fee)
            dp_1 = max(dp_1, dp_0-prices[i])
        return dp_0