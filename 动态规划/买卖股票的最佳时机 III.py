"https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/"
'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp = [[[0]*2 for _ in range(max_k+1)] for _ in range(n)] # k 可以取到2，1，0三个情况，所以要+1 
        for i in range(n):
            for k in range(max_k, 0, -1): 
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i]) # 当k=1时，k-1=0，所以遍历的时候，只要写到k=1的时候就够了。
        # 因为dp[i][k][0]表示前i天，至今最多进行k次交易，且当前不持有股票的最大利润。
        # 在此题中，最多进行两次交易，因此max_k的值为2，所以最后的结果是dp[n-1][2][0]，表示前n天，至今最多进行两次交易，且当前不持有股票的最大利润。
        # 而dp[n-1][0][0]表示前n天，至今最多进行零次交易，且当前不持有股票的最大利润，这个值一定是0，因为没有进行过任何交易，也没有持有股票。
        return dp[n-1][max_k][0] 
        
