# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-08 21:29:49
LastEditTime: 2022-03-08 21:48:29
Description: 
'''
class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i < j:
            if i< j:
                if nums[i] + nums[j] == target:
                    return [i, j]
                elif nums[i] + nums[j] < target:
                    i+=1
                else:
                    j-=1
            else:
                return
                
                    
            
s = Solution()
result = s.twoSum([1,2,3,5,7], 9)
print(result)