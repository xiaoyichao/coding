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
            # 如果 start 大于等于 end，说明数组已经排好序，返回
            if start >= end:
                return
            
            # 随机生成枢纽元素的下标
            povit_index = random.randint(start, end)
            
            # 将枢纽元素和数组末尾元素交换位置
            nums[povit_index], nums[end] = nums[end], nums[povit_index]
            # 将枢纽元素设为数组末尾元素的值
            povit = nums[end]

            # 定义两个指针 i 和 j，分别指向数组开头和结尾的元素
            i, j = start, end - 1
            # 当 i 小于等于 j 时进行循环
            while i <= j:
                # 在 i 小于等于 j 且 nums[i] 小于枢纽元素时，i 向右移动
                while i <= j and nums[i] < povit:
                    i += 1
                # 在 i 小于等于 j 且 nums[j] 大于枢纽元素时，j 向左移动
                while i <= j and nums[j] > povit:
                    j -= 1
                # 如果 i 小于等于 j，则将 nums[i] 和 nums[j] 交换位置
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                    
            # 最后将枢纽元素放到正确的位置，将数组分为两半分别递归快排
            nums[i], nums[end] = nums[end], nums[i]
            quick_sort(nums, start, i - 1)
            quick_sort(nums, i + 1, end)
        
        # 调用快速排序函数，对 nums 进行排序，起始下标为 0，结束下标为数组长度 - 1
        quick_sort(nums, 0, len(nums) - 1)
        return nums


s = Solution()
res = s.sortArray([5,2,3,1])
print(res)