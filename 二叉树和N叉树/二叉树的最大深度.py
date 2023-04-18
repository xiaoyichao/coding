# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-16 17:09:42
LastEditTime: 2023-01-26 17:11:57
Description: 

https://leetcode.cn/problems/maximum-depth-of-binary-tree/
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 深度优先搜索
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        res = max(left, right)+1
        return res

            

