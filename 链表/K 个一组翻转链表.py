"https://leetcode.cn/problems/reverse-nodes-in-k-group/"

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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



