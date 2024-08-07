"https://leetcode.cn/problems/reverse-nodes-in-k-group/"
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
<<<<<<< HEAD
    # 迭代方式
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 创建一个假的头节点，方便处理链表头的边界情况
        dummy = ListNode(0)
        dummy.next = head
        # 初始化三个指针
        pre = dummy
        cur = head
        nex = head

        # 计算链表的长度
        length = 0
        while head:
            length += 1
            head = head.next

        # 循环直到处理完整个链表
        while length >= k:
            cur = pre.next
            nex = cur.next
            # 逆转 k 个节点
            for _ in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            # 移动指针
            pre = cur
            length -= k

        return dummy.next

=======
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next
>>>>>>> origin/main

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        # 区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for i in range(k):
            # 不足 k 个，不需要反转，base case
            if not b:
                return head
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k) 
        return newHead

    """ 反转区间 [a, b) 的元素，注意是左闭右开 """
    def reverse(self, a: ListNode, b: ListNode) -> ListNode: 
        pre, cur, tmp = None, a, a
        # while 终止的条件改一下就行了
        while cur != b:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 返回反转后的头结点
        return pre



