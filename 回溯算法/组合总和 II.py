# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 17:37:37
LastEditTime: 2023-01-23 18:09:54
Description: https://leetcode.cn/problems/combination-sum-ii/
对比子集问题的解法，只要额外用一个 trackSum 变量记录回溯路径上的元素和，然后将 base case 改一改即可解决这道题：

'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        track_sum = 0
        def backtrack(nums, start, target, track_sum):
            
            if track_sum == target:
                res.append(track[:])
            if track_sum > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                track_sum +=nums[i]
                backtrack(nums, i + 1, target,track_sum)
                track_sum -= nums[i]
                track.pop()
        
        candidates.sort()
        backtrack(candidates,0,target,track_sum)

        return res

s = Solution()
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)








