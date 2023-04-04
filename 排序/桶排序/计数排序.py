# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-13 14:15:00
LastEditTime: 2022-12-13 14:15:01
Description: 在这个算法实现中，我们首先确定了元素的范围，然后初始化了一个计数数组 count，统计每个元素出现的次数。在统计完次数后，我们计算了每个元素在排序后的位置，并根据计数数组对数组进行排序。具体来说，我们遍历原始数组中的每个元素，将其放到排序数组的对应位置中，并将计数数组中对应元素的值减 1，以保证相等元素之间的顺序关系。最后，我们返回排序后的数组。
'''


def counting_sort(arr):
    # 确定元素的范围
    min_val = min(arr)
    max_val = max(arr)
    # 初始化计数数组
    count = [0] * (max_val - min_val + 1)
    # 统计每个元素出现的次数
    for num in arr:
        count[num - min_val] += 1
    # 计算每个元素在排序后的位置
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 排序数组
    sorted_arr = [0] * len(arr)
    for num in arr:
        index = count[num - min_val] - 1
        sorted_arr[index] = num
        count[num - min_val] -= 1
    return sorted_arr
