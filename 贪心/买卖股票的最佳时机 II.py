# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-07-28 21:17:56
LastEditTime: 2022-07-28 21:21:31
Description: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        for i in range(len(prices)-1):
            ans += max(0, (prices[i+1]-prices[i]))
        return ans
