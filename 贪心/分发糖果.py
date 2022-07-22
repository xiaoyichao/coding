# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-07-21 22:47:32
LastEditTime: 2022-07-22 10:26:25
Description: https://leetcode.cn/problems/candy/
'''
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
