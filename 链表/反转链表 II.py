"https://leetcode.cn/problems/reverse-linked-list-ii/description/"


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        if not head:
            return None
        
        # 定义虚拟头结点，防止left为1时需要特殊处理
        dummy = ListNode(0)
        dummy.next = head

        # 找到left节点以及left前一个节点
        p_left = head
        p_left_pre = dummy
        for i in range(1, left):
            p_left_pre = p_left
            p_left = p_left.next
        
        # 将left前一个节点与left节点分开
        p_left_pre.next = None

        # 反转右边的链表
        p = p_left
        q = p.next
        for i in range(left, right):
            temp = q.next
            q.next = p
            p = q
            q = temp

        # 将反转后的链表与左边的链表拼接
        p_left.next = q
        p_left_pre.next = p

        return dummy.next




def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    # 创建一个虚拟头结点，方便处理特殊情况
    dummy = ListNode(0)
    dummy.next = head

    # 定位到 left-1 个节点
    pre = dummy
    for i in range(left-1):
        pre = pre.next

    # 定位到第 left 个节点
    cur = pre.next

    # 逐个插入节点
    for i in range(left, right):
        # 获取下一个节点
        tmp = cur.next
        # 将下一个节点插入到 pre 和 cur 之间
        cur.next = tmp.next
        tmp.next = pre.next
        pre.next = tmp

    # 返回翻转后的链表
    return dummy.next


# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # base case
        if m == 1:
            return self.reverseN(head, n)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    successor = None # 后驱节点
    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)

        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor
        return last