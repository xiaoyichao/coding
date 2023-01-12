# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-12 18:46:43
LastEditTime: 2023-01-12 18:50:09
Description: https://leetcode.cn/problems/subsets/
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        self.backtrack(nums, 0, res)
        return res
    def backtrack(self, nums, start, res):
        res.