# coding=UTF-8
'''
Author: 
LastEditors: 
Date: 2022-08-15 22:02:02
LastEditTime: 2022-08-15 22:02:02
Description: 

插入排序
不断地从后面选一个数，然后插入到前面已经有序的序列里
时间复杂度：o(n^2)
 
希尔排序
是一种分组插入排序算法
时间复杂度：o(nlogn) ~ o(n^2)

https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/

'''
# 插入排序
def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        while (i>0):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist


# 希尔排序
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j > 0:
                if alist[j] > alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return alist