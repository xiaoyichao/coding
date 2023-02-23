# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-08-09 21:48:35
LastEditTime: 2022-08-10 23:55:14
Description: 
https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii

'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        if n == 1:
            return nums[0] == target
        l=0
        r= n-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return True
            elif nums[l] == nums[mid] and nums[mid] == nums[r]:
                # 如果 nums[l] == nums[mid] 且 nums[mid] == nums[r]，说明左、中、右三个位置的元素相等，此时将左指针加 1，右指针减 1；
                l+=1
                r-=1
            elif nums[l] <= nums[mid]:
                # 如果 nums[l] <= nums[mid]，说明左半部分是有序的，此时判断目标值是否在有序的左半部分中，如果在，则将右指针更新为 mid-1，否则将左指针更新为 mid+1；
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid +1  
            else:
                # 如果 nums[l] > nums[mid]，说明右半部分是有序的，此时判断目标值是否在有序的右半部分中，如果在，则将左指针更新为 mid+1，否则将右指针更新为 mid-1；
                if nums[mid] < target and target <= nums[r]:
                    l = mid+1
                else:
                    r =mid -1
        return False         


nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
print(s.search(nums, target))