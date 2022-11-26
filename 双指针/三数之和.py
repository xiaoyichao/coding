# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-23 17:12:51
LastEditTime: 2022-11-26 15:15:33
Description: 

https://leetcode.cn/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
现在这个写的不对，需要重新看一下，大方向是对的。
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        res = []
        for k in range(0, len(nums) -1):
            i = k+1
            j = len(nums) -1
            if(k>0 and nums[k]==nums[k-1]): # k循环的这一层去重复
                continue 
            while i<j:
                if nums[i] + nums[j] + nums[k] == 0  and i!=j and j!=k and i!=k:  
                    res.append([nums[i], nums[j], nums[k]])
                    while nums[i] == nums[i+1] and i< len(nums)-2:  # i循环的这一层去重复
                        i+=1
                    while nums[j] == nums[j-1] and j>0: # j循环的这一层去重复
                        j-=1
                    i+=1
                    j-=1
                elif nums[i] + nums[j] + nums[k]> 0 :
                    j-=1
                else:
                    i+=1

        return res


s = Solution()
nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(res)