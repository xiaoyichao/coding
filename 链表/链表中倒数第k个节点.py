# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-26 13:50:25
LastEditTime: 2022-12-26 14:12:43
Description: 
https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:  # 一次遍历，实际是两次遍历在一次中实现了
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode: # 两次遍历，遍历第二次，需要计算链表长度
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        temp = head
        for i in range(size - k):
            temp = temp.next
        return temp

