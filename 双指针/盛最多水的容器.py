# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-16 14:02:20
LastEditTime: 2022-03-16 14:03:22
Description: https://leetcode-cn.com/problems/container-with-most-water/
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))