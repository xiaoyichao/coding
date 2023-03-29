"https://leetcode.cn/problems/missing-number/"

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exprend_sum = int(n*(n+1)/2)
        actual_sum =  sum(nums)
        return exprend_sum-actual_sum