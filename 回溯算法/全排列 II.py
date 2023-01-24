# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-24 17:29:53
LastEditTime: 2023-01-24 17:52:29
Description: https://leetcode.cn/problems/permutations-ii/
排列（元素可重不可复选）
排列问题的输入如果存在重复，比子集/组合问题稍微复杂一点

对比一下之前的标准全排列解法代码，这段解法代码只有两处不同：
1、对 nums 进行了排序。
2、添加了一句额外的剪枝逻辑。但是注意排列问题的剪枝逻辑，和子集/组合问题的剪枝逻辑略有不同：新增了 !used[i - 1] 的逻辑判断。
比如 [1,2,2'] 和 [1,2',2] 应该只被算作同一个排列，所以要保证相同元素在排列中的相对位置保持不变。就会只保留下一种情况。

'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        res = []
        track = []

        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                # 相比于全排列，新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: 
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(nums)
                track.pop()
                used[i] = False
        nums.sort()    
        backtrack(nums)
        return res


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        res = []
        track = []
        

        def backtrack(nums):
            # 记录之前树枝上元素的值
            # 题目说 -10 <= nums[i] <= 10，所以初始化为特殊值
            prevNum = -666
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue

                if prevNum == nums[i]: #记录这条树枝上的值
                    continue
                used[i] = True
                track.append(nums[i])
                prevNum = nums[i]
                backtrack(nums)
                
                track.pop()
                used[i] = False
        nums.sort()    
        backtrack(nums)
        return res
s = Solution()
s.permuteUnique([1,1,2])