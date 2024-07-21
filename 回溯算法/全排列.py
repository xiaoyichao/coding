# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 16:44:31
LastEditTime: 2023-02-28 17:42:54
Description: https://leetcode.cn/problems/permutations/

排列（元素无重不可复选）
'''
from typing import List    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        truck = []
        used = [False]*len(nums)
        def backtrack(nums, track, used):
            if len(nums) == len(track):
                res.append(track[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums, track, used)
                track.pop()
                used[i] = False
        
        backtrack(nums, [], used)  
        return res  
    

#labuladong的解法
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def __init__(self):
        self.res = []

    # 主函数，输入一组不重复的数字，返回它们的全排列 
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]) -> None:

        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]:
                # nums[i] 已经在 track 中，跳过
                continue
            # 做选择
            track.append(nums[i])t
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False
# 详细解析参见：
# https://labuladong.github.io/article/?qno=46


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




s = Solution()
res = s.permute([1,2,3])
print(res)