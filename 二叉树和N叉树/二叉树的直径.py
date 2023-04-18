
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-19 13:43:28
LastEditTime: 2023-01-09 14:14:12
Description: 
https://leetcode.cn/problems/diameter-of-binary-tree/

'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0  # 初始化直径长度为0
        
        def depth(node: TreeNode) -> int:
            if not node:  # 如果节点为空，则深度为0
                return 0
            
            left_depth = depth(node.left)  # 递归计算左子树深度
            right_depth = depth(node.right)  # 递归计算右子树深度
            
            # 更新直径长度
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # 返回以当前节点为根的子树深度
            return max(left_depth, right_depth) + 1
        
        depth(root)  # 从根节点开始递归计算深度
        
        return self.diameter





class Solution:
    '''
    定义一个递归函数 dfs(node)，该函数返回一个二元组 (a, b)，其中 a 表示以 node 为根结点的子树的最大深度，b 表示以 node 为根结点的子树的直径长度。

    在递归过程中，对于每个结点 node，先递归计算其左子树和右子树的最大深度和直径长度，分别记为 (al, bl) 和 (ar, br)。

    计算以 node 为根结点的子树的最大深度 a = max(al, ar) + 1，以及直径长度 b = max(al + ar, bl, br)。其中，直径长度的计算分为三种情况：穿过 node、在左子树中、在右子树中。

    递归结束后，根据根结点的直径长度返回结果。'''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            al, bl = dfs(node.left)
            ar, br = dfs(node.right)
            a = max(al, ar) + 1
            b = max(al + ar, bl, br)
            return a, b
        
        return dfs(root)[1]


