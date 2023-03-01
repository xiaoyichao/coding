"https://leetcode.cn/problems/maximum-subarray/"

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = 0
        dp = [nums[0]]
        n = len(nums)-1
        for i in range(1, n+1):
            dp.append(max(nums[i], dp[i-1]+nums[i]))

        res = max(dp)
        return res