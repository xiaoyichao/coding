# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/submissions/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 初始化dp数组，dp[i][0]表示第i天结束时，不持有股票的最大利润，dp[i][1]表示第i天结束时，持有股票的最大利润
        dp = [[0]*2 for i in range(n)]
        for i in range(n):
            if i == 0:  # base case，第0天结束时，不持有股票的最大利润为0，持有股票的最大利润为-prices[0]
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                # 状态转移方程，如果第i天不持有股票，则dp[i][0]等于前一天不持有股票或前一天持有股票，今天卖出的利润中的最大值；
                # 如果第i天持有股票，则dp[i][1]等于前一天持有股票或前一天不持有股票，今天买入的利润中的最大值
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        # 返回最后一天结束时，不持有股票的最大利润
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

    # 奇淫做法，主要是对题目的理解，相当于每个波段的差价都赚到
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(1, n):
            res += max(0, prices[i]-prices[i-1])
        return res
