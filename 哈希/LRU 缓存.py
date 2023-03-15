"https://leetcode.cn/problems/lru-cache/?favorite=2cktkvj"


import collections
class LRUCache: # 这个方式最简单易懂

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value



import collections
class LRUCache: #其次就是这个

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key] 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
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
