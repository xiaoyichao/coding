# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-16 17:09:42
LastEditTime: 2023-01-26 17:11:57
Description: 

https://leetcode.cn/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 深度优先搜索
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 


    # def maxDepth(self, root):
    #     res = 0
    #     depth  = 0 
    #     self.traverse(root)
    #     return res

    # def traverse(self, root):
    #     if root is None:
    #         return
    #     depth +=1
    #     if root.left is None and root.right is None:
    #         res = max(res,depth)
    #     self.traverse(root.left)
    #     self.traverse(root.right)
    #     depth -=1
            

