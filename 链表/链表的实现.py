'''
在这个实现中，我们定义了两个类：ListNode 表示链表中的节点，包含节点的值和指向下一个节点的指针；LinkedList 表示链表，包含链表的头节点。


链表的基本操作包括：

is_empty()：判断链表是否为空。
add_at_head(val)：在链表头部插入一个新节点。
add_at_tail(val)：在链表尾部插入一个新节点。
add_at_index(index, val)：在链表的指定位置插入一个新节点。
delete_at_index(index)：删除链表的指定节点。
get(index)：获取链表指定位置的节点的值。
print_list()：打印链表中的所有节点的值。

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    def add_at_index(self, index, val):
        if index < 0:
            self.add_at_head(val)
        else:
            new_node = ListNode(val)
            cur_node = self.head
            for i in range(index - 1):
                if cur_node is None:
                    return
                cur_node = cur_node.next
            if cur_node is None:
                return
            new_node.next = cur_node.next
            cur_node.next = new_node

    def delete_at_index(self, index):
        if self.is_empty():
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur_node = self.head
            for i in range(index - 1):
                if cur_node.next is None:
                    return
                cur_node = cur_node.next
            if cur_node.next is None:
                return
            cur_node.next = cur_node.next.next

    def get(self, index):
        cur_node = self.head
        for i in range(index):
            if cur_node is None:
                return -1
            cur_node = cur_node.next
        if cur_node is None:
            return -1
        return cur_node.val

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.val, end=' ')
            cur_node = cur_node.next
        print()
