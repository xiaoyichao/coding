# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-30 15:53:59
LastEditTime: 2023-02-02 15:10:16
Description: https://leetcode.cn/problems/non-decreasing-array/
'''
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        l = 0 
        r = len(nums)-1

        while nums[l]<= nums[l+1] and l<len(nums)-2:
            l+=1
        if l == len(nums)-2:
            return True
        
        while nums[r-1]<= nums[r] and r>0:
            r-=1
        if r == 0:
            return True
    
        if r-l >1:
            print("a")
            return False

        if r-l<=1: 
            if l == 0 or r == len(nums)-1:
                return True
            if nums[l] <= nums[r+1] or nums[r]>=nums[l-1]:
                print("c")
                print(nums[l], nums[r])
                return True
            else:
                print("b")
                print(nums[l], nums[r])
                return False



#  左右指针的思想，但是边界情况要考虑的多一点
class Solution: 
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        l = 0
        r = len(nums)-1
        
        while l < r and nums[l] <= nums[l+1]:
            l += 1

        # 说明这是一个非递减序列，无需修改
        if l == len(nums)-1:
            return True

        while l < r and nums[r] >= nums[r-1]:
            r -= 1
        
        # 有大于1的波折 
        if r-l>1:
            return False
        #  波折发生在两端，那么修改一次即可
        if l==0 or r == len(nums)-1 :
            return True
        # 波折发生在中间，看三个数的情况，一个情况是可以修改L可以使其满足条件，第二个情况就是修改r使其满足。任何一个能满足都行
        if nums[r+1] >= nums[l] or nums[r] >=nums[l-1]:
            return True
        else:
            return False

#  滑动窗口的思想，但是也有点绕
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        count = 2
        fast = 2
        if nums[1]<nums[0]:
            count = 1
        while fast<len(nums) and count:
            if nums[fast]>=nums[fast-1]:
                # stack.append(nums[j])
                pass
            else:
                if nums[fast]<nums[fast-2]:
                    count -= 1
                    # stack.append(stack[-1])
                    nums[fast] = nums[fast-1]
                else:
                    nums[fast-1] = nums[fast-2]
                    count -= 1
                    # stack.append(nums[j])
            fast += 1
        return count>0



s =Solution()
res = s.checkPossibility([-1,4,2,3])
# res = s.checkPossibility([4,2,3])
# res = s.checkPossibility([3,4,2,3])
print(res)
