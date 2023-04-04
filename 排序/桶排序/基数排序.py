# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-13 14:15:11
LastEditTime: 2022-12-13 14:15:11
Description: 
在这个算法实现中，我们首先获取了数组中最大元素的位数，然后对每个位置进行桶排序。在桶排序的过程中，我们使用了一个桶数组 buckets，它的大小为 10，表示数字 0-9，将每个元素根据当前位置上的数字放入对应的桶中。排序完成后，我们将所有桶中的元素按照顺序合并起来，并更新原始数组。这个过程会重复进行 max_digit 次，即最大元素的位数。

'''


def radix_sort(arr):
    # 获取数组中最大元素的位数
    max_digit = len(str(max(arr)))
    # 对每个位置进行桶排序
    for i in range(max_digit):
        # 初始化桶
        buckets = [[] for _ in range(10)]
        # 将元素分配到对应的桶中
        for num in arr:
            digit = (num // (10 ** i)) % 10
            buckets[digit].append(num)
        # 合并桶中的元素，更新数组
        arr = [num for bucket in buckets for num in bucket]
    return arr
