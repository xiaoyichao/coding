# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-09 14:21:46
LastEditTime: 2023-01-27 13:16:25
Description: https://leetcode.cn/problems/binary-tree-level-order-traversal/solution/bfs-wei-shi-yao-yao-yong-dui-lie-yi-ge-s-xlpz/
'''
from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 可以使用广度优先搜索（BFS）来进行二叉树的层序遍历，通过维护一个队列来实现。

# 具体步骤如下：

# 1 将根节点加入队列。

# 2 当队列不为空时，依次取出队列中的节点，并将其左右子节点（如果存在）加入队列。

# 3 将取出节点的值记录到当前层的结果列表中。

# 4 遍历完当前层后，将结果列表加入最终结果列表中。

# 重复步骤2-4，直到队列为空。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


