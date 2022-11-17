# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2021-04-12 23:07:17
LastEditTime: 2022-11-17 18:33:02
Description:
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 解题链接：https://leetcode.cn/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): 
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast




head = [3,2,0,-4]
pos = 1

s = Solution()
print(s.hasCycle(head))
