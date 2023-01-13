# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-12 18:46:43
LastEditTime: 2023-01-13 13:15:40
Description: https://leetcode.cn/problems/subsets/
'''
from typing import List

# labuladong 的写法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        def backtrack(nums, start):
            # 遍历到了第 k 层，收集当前节点的值
            # 把当前节点放到 track 中，
            # 然后递归到下一层
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1)
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
