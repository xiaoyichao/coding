
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-14 18:32:43
LastEditTime: 2023-01-11 15:22:28
Description: 
'''

def haepfy(arr, n, i):
    '''
    Author: xiaoyichao
    Description: 建立堆
    '''   
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if i != largest:
        arr[i], arr[largest] =  arr[largest], arr[i]
        haepfy(arr, n, largest)

arr = [12, 1, 13, 5, 6, 7]
n = len(arr)
for i in range(n, -1, -1):
    haepfy(arr, n, i)
for i in range(n-1,-1,-1):
    arr[i], arr[0] = arr[0], arr[i]
    haepfy(arr, i, 0)

print(arr)