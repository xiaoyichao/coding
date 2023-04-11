"https://leetcode.cn/problems/longest-increasing-subsequence/"

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1]*n

        for i in range(n):
            for j in range(0, i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
        
