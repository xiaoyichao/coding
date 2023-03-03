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

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft() 
                vals.append(node.val)
                if node.left:  q.append(node.left)  #向队列中添加数据
                if node.right: q.append(node.right) #向队列中添加数据
            ans.append(vals)
        return ans


