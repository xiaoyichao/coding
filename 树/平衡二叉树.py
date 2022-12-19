# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-16 17:39:50
LastEditTime: 2022-12-16 17:59:02
Description: 

https://leetcode.cn/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode-solution/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 自顶向下的递归 时间复杂度：O(n^2)，其中 n 是二叉树中的节点个数。
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# 自底向上的递归 O(n)，其中 n 是二叉树中的节点个数

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if root is None: 
                return 0 
            else: 
                left_height = height(root.left) 
                right_height = height(root.right) 
                if left_height == -1 or right_height ==-1 or abs(left_height - right_height) > 1 :
                    return -1
                else:
                    return max(left_height, right_height) + 1
        return height(root) >= 0


