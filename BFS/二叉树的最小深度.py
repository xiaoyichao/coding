# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-26 17:01:19
LastEditTime: 2023-01-27 15:06:57
Description: https://leetcode.cn/problems/minimum-depth-of-binary-tree/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# labudalong 的解法
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque() #核心数据结构
        q.append(root) #将起点加入队列
        # root 本身就是一层，depth 初始化为 1
        depth = 1
        while q:
            sz = len(q)
            # 将当前队列中的所有节点向四周扩散
            for i in range(sz):
                cur = q.popleft()
                # 判断是否到达终点,也即是叶子结点
                if cur.left == None and cur.right == None:
                    return depth
                # 将 cur 的相邻节点加入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 这里增加步数，每增加一层，这里加一步，是跟for循环并列的关系
            depth += 1
        return depth


# 官方的广度优先搜索
import collections
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0

# 官方的深度优先搜索
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        
        return min_depth + 1
