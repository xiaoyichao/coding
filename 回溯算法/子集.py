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
    # 我们使用 start 参数控制树枝的生长避免产生重复的子集，用 track 记录根节点到每个节点的路径的值，
    # 同时在前序位置把每个节点的路径值收集起来，完成回溯树的遍历就收集了所有子集
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
