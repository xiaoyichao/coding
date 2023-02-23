# coding=UTF-8
'''
Author: 
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-03 08:56:37
LastEditTime: 2023-01-27 22:10:14
Description: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array

'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums,target):
            if len(nums) == 0:return -1
            left = 0
            right = len(nums)-1
            while(left<=right):
                mid = left + (right-left)//2
                if nums[mid] == target:
                    # 找到 target 时不要立即返回，而是缩小「搜索区间」的上界 right，在区间 [left, mid) 中继续搜索，即不断向左收缩，达到锁定左侧边界的目的。
                    right = mid - 1
                elif nums[mid] < target:
                    # 搜索区间变为 [mid+1, right]
                    left = mid+1
                elif nums[mid] > target:
                    # 搜索区间变为 [left, mid-1]
                    right = mid-1
                    
            if left == len(nums) : #找左边界，从左向右一直到最右边也没找到， 此时 target 比所有数都大，返回 -1
                return -1
            else: # while 里 right = mid - 1
                return right+1 if nums[right+1] == target else -1

        def right_func(nums,target):
            if len(nums) == 0:return -1
            left = 0
            right = len(nums)-1
            while(left<=right):
                mid = left + (right-left)//2
                if nums[mid] == target:
                    left = mid +1
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
            # 
            if (left-1)<0 : # 找右边界，排查到最左边的时候还是没有，此时 left - 1 索引越界
                return -1
            else: # while 里边是 left = mid +1
                return left-1 if nums[left-1] == target else -1

        a =  left_func(nums,target)
        b = right_func(nums,target)

        return [a,b]


s = Solution()
s.searchRange([2,2],3)
