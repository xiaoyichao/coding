"https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/"

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1
        while l< r:
            two_sum = numbers[l] + numbers[r]
            if two_sum< target:
                l+=1
            elif two_sum> target:
                r-=1
            elif two_sum == target:
                return [l+1, r+1]