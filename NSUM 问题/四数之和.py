'''
Author: 肖轶超 30403377+xiaoyichao@users.noreply.github.com
Date: 2023-02-20 11:20:23
LastEditors: 肖轶超 30403377+xiaoyichao@users.noreply.github.com
LastEditTime: 2023-02-20 16:24:27
FilePath: /coding-1/NSUM 问题/四数之和.py
Description: "https://leetcode.cn/problems/4sum/"
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # n 为 4，从 nums[0] 开始计算和为 target 的四元组
        return self.nSumTarget(nums, 4, 0, target)

    # 注意：调用这个函数之前一定要先给 nums 排序
    # n 填写想求的是几数之和，start 从哪个索引开始计算（一般填 0），target 填想凑出的目标和
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or sz < n:
            return res
        # 2Sum 是 base case
        if n == 2:
            # 双指针那一套操作
            lo, hi = start, sz - 1
            while lo < hi:
                # left, right = nums[lo], nums[hi]
                # sum = left + right
                sum=  nums[lo]+ nums[hi]
                if sum < target:

                    while lo < hi and nums[lo] == nums[lo + 1]: # 跳过相同的元素
                        lo += 1
                    lo += 1  # 本身的迭代
                    # 这个写法有点难理解
                    # while lo < hi and nums[lo] == left:
                    #     lo += 1

                elif sum > target:
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi-=1
                    hi-=1
                    # while lo < hi and nums[hi] == right:
                    #     hi -= 1
                   
                else:
                    res.append([nums[lo], nums[hi]])
                    # res.append([left, right])
                    while lo < hi and nums[lo] == nums[lo + 1]: # 跳过相同的元素
                        lo += 1
                    lo += 1  # 本身的迭代
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi-=1
                    hi-=1
                    # while lo < hi and nums[lo] == left:
                    #     lo += 1
                    
                    # while lo < hi and nums[hi] == right:
                    #     hi -= 1
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            for i in range(start, sz):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
                while i < sz - 1 and nums[i] == nums[i + 1]:
                    i += 1
                
        return res

s = Solution()
res = s.fourSum([1,0,-1,0,-2,2],0)