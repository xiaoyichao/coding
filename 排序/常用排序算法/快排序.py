# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:03:53
LastEditTime: 2022-08-15 22:23:05
Description:

快排的思想是，每次把第一个值作为mid_value放到数组的中间，使得mid_value左边的数都比它小，右边的数都比它大。
那么，现在可以返回mid_value的下标p，比较k（k = len(nums) - k)和p的大小，若k<p,则要找的这个数在nums[:p-1]里，若k>p, 则要找的这个数在nums[p+1:]里。

https://leetcode.cn/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/

'''
def quick_sort(alist, start, end):
    if start >= end:
        return

    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    quick_sort(li, 0, len(li)-1)
    print(li)
