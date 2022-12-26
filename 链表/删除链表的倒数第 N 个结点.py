# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-26 16:18:59
LastEditTime: 2022-12-26 16:54:45
Description: 
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        x = self.getKthFromEnd(head, n)
        x.next = x.next.next
        return dummy.next


    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:  # 一次遍历，实际是两次遍历在一次中实现了
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2