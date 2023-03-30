# 归并排序
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:04:22
LastEditTime: 2022-08-15 22:04:23
Description: 

https://leetcode.cn/problems/sort-an-array/submissions/
一句话总结就是，归并排序就是先把左半边数组排好序，再把右半边数组排好序，然后把两半数组合并。

具体来说，归并排序的过程可以分为两个步骤：分割和归并。
分割
    首先将待排序序列分成两个子序列，然后对这两个子序列进行递归分割，直到无法分割。
归并
    将两个已排好序的子序列合并成一个新的有序序列，合并过程中需要比较两个子序列中的元素，并将较小的元素放入新的序列中。

归并排序的时间复杂度为 O(nlogn)，它是一种稳定的排序算法，适用于各种数据规模的排序任务。
归并排序可以理解为二叉树的后序遍历，
执行的次数是二叉树节点的个数，每次执行的复杂度就是每个节点代表的子数组的长度，所以总的时间复杂度就是整棵树中「数组元素」的个数。
树的高度是 logN，每一层的元素个数就是序列的总长度N，所以总的时间复杂度就是O(NlogN)

归并排序是先分解再合并，从下到上解决问题。
快速排序是从上到下进行分区实现排序。

'''
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])
        # 这一步相当于后序遍历
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



        
