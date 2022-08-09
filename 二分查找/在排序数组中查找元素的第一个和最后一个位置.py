# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-08-03 08:56:37
LastEditTime: 2022-08-03 09:08:33
Description: 
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''



class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while(left<=right):
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] == target:
                    left = mid
                else:
                    left = mid+1
            if left>right:
                return -1
            else:
                return left

        def right_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while(left<=right):
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] == target:
                    left = mid
                else:
                    right = mid+1
            if left>right:
                return -1
            else:
                return left

        a =  left_func(nums,target)
        b = right_func(nums,target)

        return [a,b]