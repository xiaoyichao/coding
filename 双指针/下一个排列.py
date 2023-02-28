"https://leetcode.cn/problems/next-permutation/"
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # 从右往左遍历，找到的第一个降序的位置 ，记为i
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            # 从右往左找到第一个比nums[i]大的位置，记为j。
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i]和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, n - 1
        # 将nums[i+1:]翻转。
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


s = Solution()
res = s.nextPermutation([1, 3, 2, 5, 8, 4, 5, 6, 9])
print(res)
