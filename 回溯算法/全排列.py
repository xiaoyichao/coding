# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 16:44:31
LastEditTime: 2023-01-24 17:35:18
Description: https://leetcode.cn/problems/permutations/

排列（元素无重不可复选）
'''
from typing import List    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        res = []
        track = []

        def backtrack(nums):
            if len(track) == len(nums):
                res.append(track.copy())
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                track.append(nums[i])
                backtrack(nums)
                track.pop()
                used[i] = False
            
        backtrack(nums)
        return res

s = Solution()
res = s.permute([1,2,3])
print(res)



# 官方解法
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack()
        return res

#labuladong的解法
class Solution:
    def permute(self, nums):   
        res = [] # 结果
        def backtrack(nums, track, used):
            # track 【选择列表】，表示当前可以做的选择
            # used【路径】，记录做过的选择
            if  len(nums)==0:  # 触发结束条件， 【结束条件】就是遍历到树的底层叶子节点，也就是【选择列表】为空的时候
                res.append(used)
            for i in range(len(nums)):
                # 做选择
                track.append(nums[i])
                # 进入下一层决策树
                backtrack(nums[:i] + nums[i + 1:], track, used + [nums[i]])
                # 取消选择
                track.pop() # 返回上一层决策树
        backtrack(nums, [], [])
        return res

s = Solution()
res = s.permute([1,2,3])
print(res)