# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: 肖轶超 30403377+xiaoyichao@users.noreply.github.com
Date: 2022-11-23 17:12:51
LastEditTime: 2023-02-20 16:29:47
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
            elif _sum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1

            else:  # _sum == target
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == left:  # 跳过相同的元素
                    lo += 1

                while lo < hi and nums[hi] == right:
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

    # 排序+双指针
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
    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对原始数组进行排序
        nums.sort()
        n = len(nums)
        res = []
        
        # 枚举第一个数
        for i in range(n):
            # 如果第一个数大于0，后面的数一定大于0，直接结束循环
            if nums[i] > 0:
                break
            # 如果第一个数和前一个数相同，跳过本次循环，避免重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 双指针查找第二个数和第三个数
            left, right = i + 1, n - 1
            while left < right:
                # 如果三数之和等于0，将这三个数添加到结果列表中
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的第二个数
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 跳过重复的第三个数
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                # 如果三数之和小于0，将左指针右移
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                # 如果三数之和大于0，将右指针左移
                else:
                    right -= 1
        
        return res


s = Solution()
nums = [-1,0,1,2,-1,-4]
res = s.threeSum(nums)
print(res)


