# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-10 23:28:04
LastEditTime: 2023-01-11 13:40:51
Description: https://leetcode.cn/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
'''

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

class Solution:
    def permute(self, nums):   
        res = [] # 结果
        def backtrack(nums, track, used):
            # track 选择列表
            # used 路径
            if not nums:  # 触发结束条件
                res.append(used)
            for i in range(len(nums)):
                # 做选择
                track.append(nums[i])
                # 进入下一层决策树
                backtrack(nums[:i] + nums[i + 1:], track, used + [nums[i]])
                # 取消选择
                track.pop()
        backtrack(nums, [], [])
        return res

s = Solution()
res = s.permute([1,2,3])
print(res)