# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-27 22:00:48
LastEditTime: 2022-11-27 22:00:48
Description: 
https://leetcode.cn/problems/add-two-numbers/

解法：
链接：https://leetcode.cn/problems/add-two-numbers/solution/by-han-han-ns-fwy9/、

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表
        head = tree = ListNode()

        val = tmp = 0
        # 当三者有一个不为空时继续循环
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next
        

