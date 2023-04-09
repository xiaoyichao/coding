"https://leetcode.cn/problems/jump-game/"

from typing import List

# 这段代码更优美
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
        return max_reach >= n - 1


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False
        furthest = nums[0]
        for i in range(1, n):
            if furthest >= i:
                furthest = max(furthest, nums[i] + i)
            else:
                return False
        return furthest >= n - 1



