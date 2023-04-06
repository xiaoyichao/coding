"https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/description/"

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 哈希表存储原节点和复制节点的对应关系
        visited = {}
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        # 遍历原链表，将每个节点都复制一份，并将原节点和复制节点成对地存入哈希表中
        while old_node:
            if old_node.next:
                if old_node.next not in visited:
                    visited[old_node.next] = Node(old_node.next.val, None, None)
                new_node.next = visited[old_node.next]
            if old_node.random:
                if old_node.random not in visited:
                    visited[old_node.random] = Node(old_node.random.val, None, None)
                new_node.random = visited[old_node.random]
            old_node = old_node.next
            new_node = new_node.next

        return visited[head]
