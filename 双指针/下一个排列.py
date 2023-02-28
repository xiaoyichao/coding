"https://leetcode.cn/problems/next-permutation/"
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # 从数组的末尾开始向前搜索，找到第一个相邻的两个数 nums[i] 和 nums[i + 1]，满足 nums[i] < nums[i + 1]。
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            # 在数组的末尾开始向前搜索，找到第一个大于 nums[i] 的数 nums[j]。
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            #交换 nums[i] 和 nums[j]。
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, n - 1
        # 反转 nums[i + 1:]，使得数组按照字典序最小的顺序排列。
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


s = Solution()
res = s.nextPermutation([1,2,3])
# res = s.nextPermutation([1, 3, 2, 5, 8, 4, 5, 9, 7])
print(res)
