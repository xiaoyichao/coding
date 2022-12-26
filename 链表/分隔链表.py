# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-22 18:22:38
LastEditTime: 2022-12-22 18:54:24
Description: https://leetcode.cn/problems/partition-list/

https://labuladong.gitee.io/algo/2/19/18/

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p1 = dummy1
        p2 = dummy2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            temp = p.next
            p.next = None
            p = temp
            # p = p.next
        p2.next = None
        p1.next = dummy2.next
        
        return dummy1.next


       