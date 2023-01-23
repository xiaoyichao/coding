# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 16:44:31
LastEditTime: 2023-01-23 17:12:04
Description: https://leetcode.cn/problems/permutations/

排列（元素无重不可复选）
'''
from typing import List    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        res = []
        track = []

        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(nums)
                track.pop()
                used[i] = False
            
        backtrack(nums)
        return res

s = Solution()
res = s.permute([1,2,3])
print(res)