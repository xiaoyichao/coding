# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: 肖轶超 30403377+xiaoyichao@users.noreply.github.com
Date: 2022-11-23 17:12:51
LastEditTime: 2023-02-20 16:07:17
Description: https://leetcode.cn/problems/3sum/

'''
from typing import List


class Solution:
    # labudadong的解法
    def twoSumTarget(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        # 从 start 开始，计算有序数组 nums 中所有和为 target 的二元组
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            _sum = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if _sum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
                # 这个写法也可以
                # while lo < hi and nums[lo] == nums[lo + 1]: # 跳过相同的元素
                #     lo += 1
                # lo += 1  # 本身的迭代
            elif _sum > target:
               while lo < hi and nums[hi] == right:
                    hi -= 1
                # hi -= 1
            else: # _sum == target
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]: # 跳过相同的元素
                    lo += 1
                lo += 1 # 本身的迭代
                while lo < hi and nums[hi] == nums[hi - 1]:
                    hi -= 1
                hi -= 1
        return res


    def threeSum(self,nums: List[int],) -> List[List[int]]:
        # 对 nums 排序
        nums.sort()
        n = len(nums)
        res = []
        # 穷举 threeSum 的第一个数
        i = 0
        while i< n:
            # 对 target - nums[i] 计算 twoSum
            tuples = self.twoSumTarget(nums, i + 1, 0 - nums[i]) # for 循环那一层第i个数据，那么里边再循环的话，肯定得从i+1往后找，
            # 如果存在满足条件的二元组，再加上 nums[i] 就是结果三元组
            for tup in tuples:
                tup.append(nums[i]) #数据拼接完，送到res中。
                res.append(tup)
            # 跳过第一个数字重复的情况，否则会出现重复结果
            while i < n - 1 and nums[i] == nums[i + 1]: # for 循环这一层也得把重复的元素跳过。
                i += 1
            i += 1
        return res

    # 其他的方法
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()  
    #     res = []
    #     for k in range(0, len(nums) -1):
    #         i = k+1
    #         j = len(nums) -1
    #         if(k>0 and nums[k]==nums[k-1]): # k循环的这一层去重复
    #             continue 
    #         while i<j:
    #             if nums[i] + nums[j] + nums[k] == 0  and i!=j and j!=k and i!=k:  
    #                 res.append([nums[i], nums[j], nums[k]])
    #                 while nums[i] == nums[i+1] and i< len(nums)-2:  # i循环的这一层去重复
    #                     i+=1
    #                 while nums[j] == nums[j-1] and j>0: # j循环的这一层去重复
    #                     j-=1
    #                 i+=1
    #                 j-=1
    #             elif nums[i] + nums[j] + nums[k]> 0 :
    #                 j-=1
    #             else:
    #                 i+=1

    #     return res

s = Solution()
nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(res)


