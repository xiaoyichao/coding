# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-05-17 08:43:54
LastEditTime: 2022-12-06 14:28:17
Description: 

每一趟选出一个最大值，排在最后一个
时间复杂度：o(n^2)

https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/

'''

# 基础冒泡
def bubble_sort(alist):
    alist_len = len(alist)
    for i in range(1, alist_len):
        for j in range(0, alist_len-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

# 增加了early stop的冒泡
def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count +=1
        if count == 0: # count == 0 代表没有交换，序列已经有序，可以停止冒泡了
            break
    return alist

def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1, 0, -1):
        count = 0
        for j in range(0,i,1):
            if alist[j]>alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        if count >0:
            break
    return alist

alist = bubble_sort([1, 5, 3, 6, 3, 9, 8])
print(alist)


