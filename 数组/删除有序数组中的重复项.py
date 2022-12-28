# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-28 20:38:29
LastEditTime: 2022-12-28 20:39:30
Description: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 0 
        slow = 0
        while fast <= (len(nums)-1):
            if nums[fast] != nums[slow]:
                slow +=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1