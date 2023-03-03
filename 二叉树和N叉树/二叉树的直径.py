
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-19 13:43:28
LastEditTime: 2023-01-09 14:14:12
Description: 
https://leetcode.cn/problems/diameter-of-binary-tree/solution/

'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 求二叉树的直径
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1

        def dfs(root):
            if not root:  # 访问到空节点返回0
                return 0

            left = dfs(root.left)  # 左儿子树的深度
            right = dfs(root.right)  # 右儿子树的深度
            #  后序位置，顺便计算最大直径
            self.ans = max(self.ans, left+right+1) # 计算d_node即L+R+1 并更新ans

            return max(left, right) + 1  # 返回该节点为根的子树的深度

        dfs(root)
        return self.ans - 1  # self.ans 是节点个数，不是路径长度
