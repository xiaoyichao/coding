# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/submissions/
from typing import List


class Solution:
    # 保存整个dp
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n)]
        for i in range(n):
            if i == 0:  # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]  # 买入的话，利润就是-prices[i]
            else:
                # 状态转移方程
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[n-1][0]


    # 保存最近的两种结果
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_0 = 0
        dp_1 = 0
        for i in range(n):
            if i == 0:  # base case
                dp_0 = 0
                dp_1 = -prices[i]  # 买入的话，利润就是-prices[i]
            else:
                # 状态转移方程
                dp_1 = max(dp_1,  dp_0-prices[i])
                dp_0 = max(dp_0, dp_1+prices[i])
        return dp_0
