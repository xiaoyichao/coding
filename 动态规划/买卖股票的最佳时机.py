'''给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock

解法：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m'''

from typing import List
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][0] = 


    # def maxProfit(self, prices: List[int]) -> int:
    #     min_price = float("inf")
    #     max_profit = 0
    #     for price in prices:
    #         min_price = min(min_price, price)
    #         max_profit = max(max_profit, price-min_price)
    #     return max_profit
        

s = Solution()
res = s.maxProfit([7,1,5,3,6,4])
print(res)