# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-29 23:36:35
LastEditTime: 2022-12-29 23:36:35
Description: https://leetcode.cn/problems/move-zeroes/
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast = 0
        slow = 0
        while fast<len(nums) :
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow+=1
            fast +=1
        while slow< len(nums):
            nums[slow]=0
            slow+=1
        return nums