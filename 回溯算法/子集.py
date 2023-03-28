# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-12 18:46:43
LastEditTime: 2023-01-23 17:12:29
Description: https://leetcode.cn/problems/subsets/

子集（元素无重不可复选）
'''
from typing import List

# labuladong 的写法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        track = []

        def backtrack(nums, start):
            res.append(track[:])
            
            for i in range(len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()
            
        backtrack(nums, 0)
        return res



s = Solution()
s.subsets([1,2,3])

# 其他人的写法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        n = len(nums)
        def backtrack(i: int) -> None:
            res.append(track.copy())  # 固定答案
            if i == n:
                return
            for j in range(i, n):  # 枚举选择的数字
                track.append(nums[j])
                backtrack(j + 1)
                track.pop()  # 恢复现场
        backtrack(0)
        return res



s = Solution()
s.subsets([1,2,3])
