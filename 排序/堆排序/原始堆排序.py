'''
堆排序由Floyd和Williams在1964年共同发明，是对简单选择排序算法的优化，其出发点是：简单选择排序在遍历时，在待排序的n个元素中，需进行n-1次比较，
才能选择出最小的元素，但没有将每次遍历时比较的结果保存下来，导致后续遍历时仍需进行重复操作，因此导致元素比较次数较多。

堆排序（Heap Sort）是一种高效的排序算法，基于堆（Heap）的数据结构实现。堆是一种特殊的树形数据结构，它满足以下两个条件：

堆是一棵完全二叉树。
堆中每个节点的值都大于等于（或小于等于）其子节点的值，这种关系被称为堆的性质。
在堆排序中，我们首先需要构建一个最大堆（或最小堆），然后将堆顶元素（也就是最大值或最小值）与堆底元素交换，再将剩余的元素重新调整为最大堆（或最小堆），重复这个过程直到所有元素有序排列。

堆排序的具体步骤如下：

构建最大堆（或最小堆）：从最后一个非叶子节点开始，将每个节点与其子节点比较，如果不满足堆的性质则进行交换，直到整个堆满足堆的性质。
将堆顶元素（最大值或最小值）与堆底元素交换，将堆的大小减一。
重新调整剩余元素为最大堆（或最小堆），重复步骤2直到堆的大小为1。
堆排序的时间复杂度为$O(n\log n)$，空间复杂度为$O(1)$，因此它是一种原地排序算法。它的优点是不受输入数据的影响，稳定性较好，适用于大数据量的排序。

'''


def heapify(arr, n, i):
    '''
    Author: xiaoyichao
    Description: 对数组arr[:n] 建立堆，初始化的时候以arr[i]为堆顶
    '''
    largest = i
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    if l < n and arr[i] < arr[l]: # l < n 
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)  # 递归函数尽量不要写返回值


def heapSort(arr):

    n = len(arr)

    # Build a maxheap. 首次建立堆
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 一个个交换元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # 交换第一个和第i个元素，打乱堆之后，然后重新建堆。
        heapify(arr, i, 0)  # 对arr[:i] 建堆，因为arr[i:]已经排序好了


arr = [12, 1, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
print(arr)
