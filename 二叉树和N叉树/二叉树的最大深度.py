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
        # 定义递归函数，通过分解成子问题，通过子问题（子树）的答案推导出原问题的答案
        res = 0
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        res = max(left, right)+1
        return res

# 遍历的思路，用一个 traverse 函数配合外部变量来实现，
class Solution:
    def __init__(self):
        self.res = 0
        self.depth = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res
    
    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.depth += 1
        
        if not root.left and not root.right:
            self.res = max(self.res, self.depth)
        
        self.traverse(root.left)
        self.traverse(root.right)
        
        self.depth -= 1