
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-15 15:16:44
LastEditTime: 2022-12-15 16:23:03
Description: 
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
https://leetcode.cn/problems/reverse-linked-list/


'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse_list(self, head):
        
        """
        双指针迭代法
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

    def reverseList(self, head):
        '''
        递归法
        Author: xiaoyichao
        Description: 
        '''   
        if(head==None or head.next==None):  # 如果链表为空或链表只有一个节点，直接返回
            return head
        
        cur = self.reverseList(head.next)  # 递归调用reverseList函数，反转剩余节点
    
        head.next.next = head  # 反转当前节点
        head.next = None  # 将当前节点指向下一个节点的指针断开
        
        return cur  # 返回反转后的链表头节点
