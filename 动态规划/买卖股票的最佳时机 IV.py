# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-02-03 13:52:50
LastEditTime: 2023-02-06 15:01:21
Description: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，第三个是当前的持有状态即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）。然后我们用一个三维数组就可以装下这几种状态的全部组合：

给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


'''
from typing import List


# labuladong 的解法
class Solution:
    def maxProfit(self, max_k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0:
            return 0
        if max_k > n // 2:
            # 交易次数 k 没有限制的情况，买卖不能在同一天发生，所以最大交易次数限制>天数//2的时候，相当没有交易次数的限制。
            return self.maxProfit_k_inf(prices)

        # 假如你可最多交易2次，那当前，你可能，还可以交易0，1，2次三个可能。所以k的维度要取到K的右闭区间。
        # 我们先创建一个三维的空数组，每个元素都是0
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        
        for i in range(n):
            for k in range(max_k, 0, -1):
                if i == 0:  #base case
                    # i = 0 的时候，没办法计算i-1的情况了，这是 base case。
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:    
                    # 状态转移方程
                    # 第i天，不持有股票，还可以交易k次 = max（【i-1天，还可以交易k次，未持有】，【i-1天，还可以交易k次，持有，但是会卖出，k在买入的动作计数，卖出的时候不计数】
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i]) 
                    # 第i天，不持有股票，还可以交易k次 = max（【昨天和今天的状态一样】，【昨天买入】） 买入的时候，k的计数要变化。
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k][0]

    # 第 122 题，k 无限的解法
    def maxProfit_k_inf(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

        
k = 2
prices = [3,2,6,5,0,3]
s = Solution()
res = s.maxProfit(k,prices)
prices(s)

# chatGPT 写的代码
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        if k >= n//2:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i]-prices[i-1])
            return res
        
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxDiff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
        return dp[k][n-1]
