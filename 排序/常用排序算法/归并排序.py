# 归并排序
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:04:22
LastEditTime: 2022-08-15 22:04:23
Description: 

https://leetcode.cn/problems/sort-an-array/submissions/
拆分到单个元素，然后两个两个往上进行递归合并。设置left 和right两个游标,进行合并。
时间复杂度：o(nlogn)

冒泡排序、插入排序、选择排序这三种排序算法，它们的时间复杂度都是 O(n2)，比较高，适合小规模数据的排序。归并排序和快速排序的时间复杂度为 O(nlogn) 。这两种排序算法适合大规模的数据排序

稳定，但是，归并排序并没有像快排那样，应用广泛，这是为什么呢？因为它有一个致命的“弱点”，那就是归并排序不是原地排序算法。
这是因为归并排序的合并函数，在合并两个有序数组为一个有序数组时，需要借助额外的存储空间。

'''
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self, left, right):
        res = []
        i, j = 0,0
        while i<len(left) and j< len(right):
            if left[i]<= right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res = res+left[i:]
        res = res+right[j:]
        return res



        
