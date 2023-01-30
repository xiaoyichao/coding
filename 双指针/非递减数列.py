# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-30 15:53:59
LastEditTime: 2023-01-30 16:40:18
Description: https://leetcode.cn/problems/non-decreasing-array/
'''
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = 0
        r = 0
        valid = 0
        d = nums[0]
        while r < len(nums):
            c = nums[r]
            r += 1
            # if c < d:
            #     valid += 1

            while (r-l > 0):

                if valid > 1:
                    return False

                d = nums[l]
                l += 1
                if c < d:
                    valid += 1





                
        return True

s =Solution()
res = s.checkPossibility([3,4,2,3])
print(res)
