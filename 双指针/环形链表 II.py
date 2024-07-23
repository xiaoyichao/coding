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




head = [3,2,0,-4]
pos = 1

s = Solution()
print(s.hasCycle(head))
