# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-05-17 08:43:54
LastEditTime: 2022-08-16 22:39:53
Description: 

每一趟选出一个最大值，排在最后一个
时间复杂度：o(n^2)

https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/

'''


def bubble_sort(alist):
    alist_len = len(alist)
    count

    for i in range(1, alist_len):
        for j in range(0, alist_len-i):

            
            
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
    return alist


alist = bubble_sort([1, 5, 3, 6, 3, 9, 8])
print(alist)


