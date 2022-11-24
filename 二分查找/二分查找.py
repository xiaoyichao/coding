# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-23 15:31:09
LastEditTime: 2022-11-23 15:33:23
Description: 

链接：https://leetcode.cn/problems/binary-search/solution/py-by-mou-6d-uavv/

'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return -1

nums = [-1,0,3,5,9,12]
target = 9
s = Solution()
res = s.search(nums, target)
print(nums[res])