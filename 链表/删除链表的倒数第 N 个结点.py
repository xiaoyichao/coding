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
        dummy = ListNode(0)  # 创建虚拟头结点
        dummy.next = head  # 将虚拟头结点指向原链表的头结点
        fast = slow = dummy  # 创建两个指针fast和slow，并且初始值均为虚拟头结点
        for i in range(n):  # fast指针先走n步
            fast = fast.next
        while fast.next:  # 当fast指针走到链表末尾时，slow指针指向待删除节点的前一个节点
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # 将待删除节点的前一个节点的next指向待删除节点的后一个节点，即跳过待删除节点
        return dummy.next  # 返回虚拟头结点的next指针，即为新的链表的头结点



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
    

