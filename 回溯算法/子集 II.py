# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 17:20:12
LastEditTime: 2023-01-23 17:35:03
Description: https://leetcode.cn/problems/subsets-ii/
子集/组合（元素可重不可复选）
按照之前的思路画出子集的树形结构，显然，两条值相同的相邻树枝会产生重复：
体现在代码上，需要先进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过
'''
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        
        def backtrack(nums, start):
            res.append(track[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()

        nums.sort()
        backtrack(nums,0)
        return res

s = Solution()
res = s.subsetsWithDup([1,2,2])
print(res)

