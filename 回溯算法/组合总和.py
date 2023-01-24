# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-24 17:53:51
LastEditTime: 2023-01-24 18:00:15
Description: https://leetcode.cn/problems/combination-sum/
子集/组合（元素无重可复选）
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        track_sum = 0
        def backtrack(nums, start, target, track_sum):
            # base case，找到目标和，记录结果
            if track_sum == target:
                res.append(track[:])
            # base case，超过目标和，停止向下遍历
            if track_sum > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                track_sum +=nums[i]
                # 这个 i 从 start 开始，那么下一层回溯树就是从 start + 1 开始，从而保证 nums[start] 这个元素不会被重复使用：
                # 那么反过来，如果我想让每个元素被重复使用，我只要把 i + 1 改成 i 即可：
                # 这相当于给之前的回溯树添加了一条树枝，在遍历这棵树的过程中，一个元素可以被无限次使用：
                backtrack(nums, i, target,track_sum)
                track_sum -= nums[i]
                track.pop()
        
        candidates.sort()
        backtrack(candidates,0,target,track_sum)

        return res

s = Solution()
s.combinationSum(candidates = [2,3,6,7], target = 7)
