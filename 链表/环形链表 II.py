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
        # 初始化两个指针，slow 和 fast，均指向链表的头结点
        slow = head
        fast = head
        
        # 使用快慢指针法，fast 每次移动两步，slow 每次移动一步
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # 如果 fast 和 slow 相遇，说明链表中存在环
            if fast == slow:
                break
        
        # 如果 fast 指针到达链表末端，说明链表中没有环
        if fast is None or fast.next is None:
            return None
        
        # 将 fast 指针重新指向链表头部，slow 保持在相遇点
        fast = head
        
        # fast 和 slow 每次都移动一步，当它们再次相遇时，即为环的入口点
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        # 返回环的入口点
        return slow
