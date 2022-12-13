# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-07-28 21:17:56
LastEditTime: 2022-12-13 14:36:30
Description: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
贪心或者动态规划，都可以
这个是区间问题

'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        for i in range(len(prices)-1):
            ans += max(0, (prices[i+1]-prices[i]))
        return ans
