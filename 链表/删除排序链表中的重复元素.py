# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-28 21:34:11
LastEditTime: 2022-12-28 21:34:12
Description: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next

        return head