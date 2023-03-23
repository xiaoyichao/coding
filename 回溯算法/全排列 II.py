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
        # 标记元素是否被使用过
        used = [False]*len(nums)
        # 存储结果的数组
        res = []
        # 存储当前的排列
        track = []
        
        def backtrack(nums):
            # 如果当前排列的长度和数组的长度相等，则找到一组排列，将其加入结果数组中
            if len(track) == len(nums):
                res.append(track.copy())
                return
            # 遍历每个元素，尝试将其加入排列中
            for i in range(len(nums)):
                # 如果元素已经被使用过，则跳过
                if used[i]:
                    continue
                # 如果当前元素和前一个元素相等，并且前一个元素未被使用过，则跳过当前元素
                # 为了避免生成重复的排列，我们需要对输入数组进行排序，并且在生成排列时，如果发现当前元素和前一个元素相等，并且前一个元素未被使用过，则跳过当前元素。
                # 这样做的原因是，如果前一个元素未被使用过，则说明前一个元素已经被回溯回来，已经从当前排列中弹出。如果当前元素和前一个元素相等，则说明当前元素已经在前一个元素的分支中被加入到了排列中。在这种情况下，我们不应该再将当前元素加入到排列中，以避免生成重复的排列。
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # 标记当前元素已被使用过
                used[i] = True
                # 将当前元素加入排列中
                track.append(nums[i])
                
                # 继续尝试加入下一个元素
                backtrack(nums)
                # 回溯，将最后加入的元素弹出
                track.pop()
                # 标记当前元素未被使用过
                used[i] = False
        # 对数组进行排序，以便后续去重操作
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