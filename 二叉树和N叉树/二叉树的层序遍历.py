# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-09 14:21:46
LastEditTime: 2023-01-27 13:16:25
Description: https://leetcode.cn/problems/binary-tree-level-order-traversal/
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
        # 如果根节点为空，返回空列表
        if not root:
            return []
        # 初始化结果列表和队列
        res = []
        queue = [root]
        # 当队列不为空时，依次取出队列中的节点，并将其左右子节点（如果存在）加入队列。
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
            # 将取出节点的值记录到当前层的结果列表中。
            res.append(level)
        # 遍历完当前层后，将结果列表加入最终结果列表中。
        return res


    
# 当然，如果使用队列也可以。deque 是基于双端链表实现的，比list更快
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level = []
            tmp_size = len(queue)
            for _ in range(tmp_size):
                cur_node = queue.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(level)
        return res

