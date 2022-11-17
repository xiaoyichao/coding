# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-16 10:25:14
LastEditTime: 2022-03-16 10:57:16
Description: https://leetcode-cn.com/problems/merge-sorted-array/

本质是两个指针，但是因为在原地修改，所以是三个指针
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n-1
        tail = m+n-1
        while tail > -1:
            if p1 == -1:  # 一定要先判断前两个情况，因为后两个情况在前两个情况的时候也是成立的。
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        return nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n-1
        j = m-1
        tmp =  len(nums1)-1
        while tmp > -1:
            if j==-1:
                nums1[tmp] = nums2[i]
                i-=1
            elif i==-1:
                nums1[tmp] = nums1[j]
                j-=1
            elif nums1[j] > nums2[i]:
                nums1[tmp] = nums1[j]
                j-=1
            else:
                nums1[tmp] = nums2[i]
                i-=1

            tmp -=1
        return nums1


solution = Solution()
print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
