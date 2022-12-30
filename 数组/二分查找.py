# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-29 23:44:13
LastEditTime: 2022-12-29 23:44:13
Description: https://leetcode.cn/problems/binary-search/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                left = mid +1
            else:
                right = mid -1
        return -1