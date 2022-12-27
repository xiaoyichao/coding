# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-27 18:59:08
LastEditTime: 2022-12-27 19:44:34
Description: 
https://leetcode.cn/problems/linked-list-cycle-ii/

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                break
        if fast is None or fast.next is None :
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow