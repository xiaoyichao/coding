# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-29 23:28:32
LastEditTime: 2022-12-29 23:36:19
Description: https://leetcode.cn/problems/remove-element/
'''
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0 
        slow = 0
        while(fast<len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow
s = Solution()
s.removeElement([3,2,2,3], 3)
