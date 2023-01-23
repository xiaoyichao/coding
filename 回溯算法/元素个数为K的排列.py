# coding=UTF-8
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 17:04:54
LastEditTime: 2023-01-23 17:12:08
Description: 
'''
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 16:44:31
LastEditTime: 2023-01-23 17:03:47
Description: https://leetcode.cn/problems/permutations/

排列（元素无重不可复选）
'''
from typing import List    

class Solution:
    def permute(self, nums: List[int], k:int) -> List[List[int]]:
        used = [False]*len(nums)
        res = []
        track = []

        def backtrack(nums, k):
            if len(track) == k:
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(nums,k)
                track.pop()
                used[i] = False
            
        backtrack(nums, k)
        return res

s = Solution()
res = s.permute([1,2,3],2)
print(res)