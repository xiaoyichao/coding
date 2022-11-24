# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-23 17:12:51
LastEditTime: 2022-11-23 20:37:13
Description: 

https://leetcode.cn/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
现在这个写的不对，需要重新看一下，大方向是对的。
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        j = len(nums) -1
        k = 0
        res = []
        for k in range(0, len(nums) -1):
            while i<j:
                if nums[i] + nums[j] <  - nums[k]:  
                    i+=1
                elif nums[i] + nums[j] >  - nums[k]:
                    j-=1
                else:
                    if i!=j and i!=k and j!=k:
                        res.append([nums[i], nums[j], nums[k]])
                        break
        return res