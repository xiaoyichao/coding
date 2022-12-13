# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:03:53
LastEditTime: 2022-12-13 13:57:36
Description:

https://blog.csdn.net/weixin_43250623/article/details/88931925

快速排序算法其实很简单，采用分治策略。步骤如下：

选取一个基准元素（pivot）
比pivot小的放到pivot左边，比pivot大的放到pivot右边
对pivot左边的序列和右边的序列分别递归的执行步骤1和步骤2

快速排序也是用到了分治思想和递归实现方式，这一点跟归并排序是一样的，但是快速排序的实现跟归并是完全不一样的。
归并排序是先分解再合并，从下到上解决问题。
快速排序是从上到下进行分区实现排序。

'''


def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] <= mid:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后


def quick_sort_1(alist, start, end):
    if start >= end:
        return
    middle = start
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= alist[middle]:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= alist[middle]:
            low += 1
        alist[high] = alist[low]
    alist[low] = alist[middle]
    quick_sort_1(alist, start, low-1)
    quick_sort_1(alist, low+1, end)


def quick_sort_2(alist, start, end):
    if start >= end:
        return
    middle = start
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= alist[middle]:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] <= alist[middle]:
            low += 1
        alist[high] = alist[low]
    alist[low] = alist[middle]
    quick_sort_2(alist, low+1, end)
    quick_sort_2(alist, start, low-1)


if __name__ == '__main__':
    alist = [54, 54, 93, 66, 66, 31, 44, 55, 55]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
    alist = [54, 54, 93, 66, 66, 31, 44, 55, 55]
    quick_sort_1(alist, 0, len(alist)-1)
    print(alist)


