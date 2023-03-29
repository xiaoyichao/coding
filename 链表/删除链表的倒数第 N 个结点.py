# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-26 16:18:59
LastEditTime: 2022-12-27 17:55:19
Description: 
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        for i in range(n):
            p1 = p1.next
        
        if not p1:
            return head.next
        
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return head
    
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

