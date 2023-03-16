# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:03:53
LastEditTime: 2022-12-13 13:57:36
Description:

https://leetcode.cn/problems/sort-an-array/submissions/

快速排序算法其实很简单，采用分治策略。步骤如下：

选取一个基准元素（pivot）
比pivot小的放到pivot左边，比pivot大的放到pivot右边
对pivot左边的序列和右边的序列分别递归的执行步骤1和步骤2

快速排序也是用到了分治思想和递归实现方式，这一点跟归并排序是一样的，但是快速排序的实现跟归并是完全不一样的。
归并排序是先分解再合并，从下到上解决问题。
快速排序是从上到下进行分区实现排序。

'''
import random
from typing import List

class Solution: # 建议用这个
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            pivot = random.choice(nums)
            left = []
            right = []
            mid = []
            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num == pivot:
                    mid.append(num)
                else:
                    right.append(num)
            return self.sortArray(left) + mid + self.sortArray(right)


import random
class Solution:  #快排序
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, start, end):
            if start >= end:
                return

            # 将随机主元移动到最后一个位置
            povit_index = random.randint(start, end)
            nums[povit_index], nums[end] = nums[end], nums[povit_index]

            povit = nums[end]
            i,j = start, end-1
            while i<=j:
                while i<=j and nums[j]>povit:
                    j-=1
                while i<=j and nums[i]<povit:
                    i+=1
                if i<=j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j-=1
            nums[i], nums[end] = nums[end], nums[i]
            quick_sort(nums, start, i-1)
            quick_sort(nums, i+1, end)
        
        quick_sort(nums, 0, len(nums)-1)
        return nums


s = Solution()
res = s.sortArray([5,2,3,1])
print(res)