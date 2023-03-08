'''
堆排序由Floyd和Williams在1964年共同发明，是对简单选择排序算法的优化，其出发点是：简单选择排序在遍历时，在待排序的n个元素中，需进行n-1次比较，
才能选择出最小的元素，但没有将每次遍历时比较的结果保存下来，导致后续遍历时仍需进行重复操作，因此导致元素比较次数较多。

堆排序就是通过堆这种结构，实现了在选择出最小元素的同时，保存了比较结果，用于后续的操作，从而减少比较次数，提高排序效率。

堆是具有下列性质的完全二叉树：每个结点的值都大于或等于其左右孩子的值，称为大顶堆；或每个结点的值都小于或等于其左右孩子的值，称为小顶堆。

将待排序的数组初始化为大顶堆，该过程即建堆。
将堆顶元素与最后一个元素进行交换，除去最后一个元素外可以组建为一个新的大顶堆。
由于第二部堆顶元素跟最后一个元素交换后，新建立的堆不是大顶堆，需要重新建立大顶堆。重复上面的处理流程，直到堆中仅剩下一个元素。

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
