# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-15 17:51:42
LastEditTime: 2022-12-20 20:35:26
Description: 
https://leetcode.cn/problems/merge-two-sorted-lists/

链接：https://leetcode.cn/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代，本质是使用了双指针+单指针
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1) #将头节点的val置为-1，当然也可以置为其他数 
        prev = prehead
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1 # l1的指针下移
                list1 = list1.next
            else:
                prev.next = list2 # l2的指针下移 
                list2 = list2.next
            prev = prev.next # 单指针下移 
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        if list1:
            prev.next = list1 
        else:
            prev.next = list2
        return prehead.next # 不要头节点



class Solution:
    # 递归
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


