# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-07-21 22:47:32
LastEditTime: 2022-07-22 10:26:25
Description: https://leetcode.cn/problems/candy/

n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

这个也是一个分配问题
'''

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        len_ratings = len(ratings)
        list_sum = [1] * len_ratings
        
        for i in range(1, len_ratings,1):
            if ratings[i] > ratings[i-1]:
                list_sum[i] = list_sum[i-1] +1
        for i in range(len_ratings-2, -1, -1):
            if ratings[i] > ratings[i+1] :
                list_sum[i] = max(list_sum[i],list_sum[i+1] + 1)
    
        return sum(list_sum)
