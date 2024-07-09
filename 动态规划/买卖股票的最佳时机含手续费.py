"https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/"
'''
给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
'''
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