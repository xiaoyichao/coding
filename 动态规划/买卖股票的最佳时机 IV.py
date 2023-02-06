# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-02-03 13:52:50
LastEditTime: 2023-02-06 15:01:21
Description: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

这个问题的「状态」有三个，第一个是天数，第二个是允许交易的最大次数，第三个是当前的持有状态即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）。然后我们用一个三维数组就可以装下这几种状态的全部组合：



'''
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] 
        dp[-1][...][0] = 0
        # 解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0。

        dp[-1][...][1] = -float('inf')
        # 解释：还没开始的时候，是不可能持有股票的。
        # 因为我们的算法要求一个最大值，所以初始值设为一个最小值，方便取最大值。

        dp[...][0][0] = 0
        # 解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0。

        dp[...][0][1] = -float('inf')
        # 解释：不允许交易的情况下，是不可能持有股票的。
        # 因为我们的算法要求一个最大值，所以初始值设为一个最小值，方便取最大值。

        # 状态转移方程
        dp[]

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
