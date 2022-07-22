# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-05-13 09:15:16
LastEditTime: 2022-05-13 09:35:26
Description: https://leetcode.cn/problems/kth-largest-element-in-an-array/

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        num = nums[k-1]
        return num


solution = Solution()
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
