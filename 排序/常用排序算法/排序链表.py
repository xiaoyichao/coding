"https://leetcode.cn/problems/sort-list/?favorite=2cktkvj"

# 将链表不断地分成左右两部分，直到每个部分只有一个节点或者为空，然后进行合并。
# 合并时，比较左右两部分的节点值，将小的节点先放入新的链表中，然后继续比较剩余的节点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 快慢指针找到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None  # 分割成两个链表

        # 递归排序左右两部分
        left, right = self.sortList(head), self.sortList(mid)

        # 合并已排序的左右两部分
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next, left = left, left.next
            else:
                cur.next, right = right, right.next
            cur = cur.next
        cur.next = left if left else right

        return dummy.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow,fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        mid, slow.next = slow.next, None

        left,right =  self.sortList(head), self.sortList(mid)

        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur= cur.next
        if left:
            cur.next = left
        else:
            cur.next = right

        return dummy.next