"https://leetcode.cn/problems/search-in-rotated-sorted-array/?favorite=2cktkvj"


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # 二分查找循环条件
            mid = (left + right) // 2  # 找到中间位置
            if nums[mid] == target:  # 如果中间位置的值等于目标值，直接返回该位置
                return mid
            if nums[mid] >= nums[left]:  # 如果中间位置的值大于等于最左边的值，说明左半部分数组有序
                if nums[left] <= target < nums[mid]:  # 如果目标值在左半部分数组中，缩小查找范围到左半部分数组
                    right = mid - 1
                else:  # 如果目标值不在左半部分数组中，缩小查找范围到右半部分数组
                    left = mid + 1
            else:  # 如果中间位置的值小于最左边的值，说明右半部分数组有序
                if nums[mid] < target <= nums[right]:  # 如果目标值在右半部分数组中，缩小查找范围到右半部分数组
                    left = mid + 1
                else:  # 如果目标值不在右半部分数组中，缩小查找范围到左半部分数组
                    right = mid - 1
        return -1  # 如果找不到目标值，返回 -1
