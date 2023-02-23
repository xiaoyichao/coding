from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return self.__str__()
    
    def is_leaf(self):
        return not (self.left or self.right)
    
    def height(self):
        if self.is_leaf():
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)
    
    def size(self):
        if self.is_leaf():
            return 1
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size


class Solution:
    def dfs(self, graph, start, visited):
        if start not in visited:
            visited.add(start)
            # TODO: 在这里进行节点处理操作
            print(start.val)
            for neighbor in graph[start]:
                self.dfs(graph, neighbor, visited)


class Solution:
    def bfs(self, graph, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                # TODO: 在这里进行节点处理操作
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}
solution = Solution()
visited = set()
start_node = 1
solution.dfs(graph, start_node, visited)
