# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-29 23:48:37
LastEditTime: 2022-12-29 23:48:37
Description: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]< target:
                i+=1
            elif numbers[i]+numbers[j]> target:
                j-=1
            else:
                return [i+1,j+1]