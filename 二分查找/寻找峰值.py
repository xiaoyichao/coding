'''
https://leetcode.cn/problems/find-peak-element/description/

峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。


'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        def get_num(i):
            if i < 0 or i >= n:
                return float('-inf')
            return nums[i]
        
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if get_num(mid - 1) < get_num(mid) > get_num(mid + 1):
                return mid
            
            if get_num(mid) < get_num(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
