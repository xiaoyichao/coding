# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-23 15:31:09
LastEditTime: 2023-01-27 19:41:07
Description: 

链接：https://leetcode.cn/problems/binary-search/submissions/
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
s = Solution()
res = s.search(nums, target)
print(nums[res])