# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-05-17 09:11:03
LastEditTime: 2022-05-17 09:12:32
Description: 
作者：xiao-xie-shui-bu-xing
链接：https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

每一趟选出一个最小值，放到前面
时间复杂度：o(n^2)
'''


def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


alist = select_sort([1, 5, 3, 6, 3, 9, 8])
print(alist)
