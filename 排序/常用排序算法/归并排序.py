# 归并排序
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:04:22
LastEditTime: 2022-08-15 22:04:23
Description: 

拆分到单个元素，然后两个两个往上进行递归合并。设置left 和right两个游标,进行合并。
时间复杂度：o(nlogn)

https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/

'''
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    left_point,right_point = 0,0
    result = []
    while left_point < len(left) and right_point < len(right):
        if left[left_point] <= right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result += left[right_point:]
    result += right[left_point:]
    return result
