# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-08-15 22:02:02
LastEditTime: 2022-11-23 15:19:53
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
    #  对比当前数字和已经排序的数据，大小不合适就换，就像冒泡，直到位置合适就break
    len_alist = len(alist)
    for i in range(1, len_alist):
        while i>0 :
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i-=1
            else:
                break
    return alist

def insert_sort(alist):
    len_alist = len(alist)
    for i  in range(1,len_alist-1):
        while i >0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i-=1
            else:
                break
        
    return alist


print(insert_sort([1,4,2,5,7,2,6,8,29]))

# 希尔排序 将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return alist


print(shell_sort([1,4,2,5,7,2,6,8,29]))