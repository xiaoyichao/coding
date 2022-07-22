# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-05-17 08:43:54
LastEditTime: 2022-05-17 09:10:21
Description: 
作者：xiao-xie-shui-bu-xing
链接：https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

每一趟选出一个最大值，排在最后一个
时间复杂度：o(n^2)

'''


def bubble_sort(alist):
    alist_len = len(alist)
    for i in range(1, alist_len):
        for j in range(0, alist_len-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                count += 1
    return alist


alist = bubble_sort([1, 5, 3, 6, 3, 9, 8])
print(alist)


