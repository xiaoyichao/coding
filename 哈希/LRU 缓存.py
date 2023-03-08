"https://leetcode.cn/problems/lru-cache/?favorite=2cktkvj"


import collections

# labuladong
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict() 
        #OrderedDict直接实现了双向链表和哈希表，牛啊。直接省事了

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 将 key 变为最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 修改 key 的值
            self.cache[key] = value
            # 将 key 变为最近使用
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.cap:
            # 链表头部就是最久未使用的 key
            self.cache.popitem(last=False)
        # 将新的 key 添加链表尾部
        self.cache[key] = value


class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

# chatgpt 的解法
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                del self.cache[removed.key]
                self.size -= 1

    def add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: Node) -> None:
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self) -> Node:
        node = self.tail.prev
        self.remove_node(node)
        return node
