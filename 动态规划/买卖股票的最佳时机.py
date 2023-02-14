'''给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock

解法：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m'''

from typing import List
class Solution:

    # 这是自底向上的迭代方式的动态规划，保留所有DP
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i-1==-1: #base case 第一天的状态
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                # 当天没有持有= max(昨天没持有，昨天持有但是今天卖掉)
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) 
                # 当天持有 = max(之前买了但今天也没有卖，之前没买但是今天买了)
                dp[i][1] = max(dp[i-1][1], -prices[i])
        # 最后一天手里肯定是没持有股票的情况比持有的情况更赚钱。   
        return dp[-1][0]

    # 不需要用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float("inf")
        for i in range(n):
            # 当天没有持有= max(昨天没持有，昨天持有但是今天卖掉)
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i]) 
            # 当天持有 = max(之前买了但今天也没有卖，之前没买但是今天买了)
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0
        
    # 这是自底向上的迭代方式的动态规划，只保留最近的结果，没保留所有DP
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit
        

s = Solution()
res = s.maxProfit([7,1,5,3,6,4])
print(res)