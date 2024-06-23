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
        # 我们让慢指针 slow 走在后面，快指针 fast 走在前面探路，找到一个不重复的元素就赋值给 slow 并让 slow 前进一步。
        # 这样，就保证了 nums[0..slow] 都是无重复的元素，当 fast 指针遍历完整个数组 nums 后，nums[0..slow] 就是整个数组去重之后的结果。
        fast = 0 
        slow = 0
        while fast <= (len(nums)-1):
            if nums[fast] != nums[slow]:
                slow +=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1