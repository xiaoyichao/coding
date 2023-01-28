# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-27 19:15:08
LastEditTime: 2023-01-28 10:52:00
Description: https://leetcode.cn/problems/n-ary-tree-postorder-traversal/
'''
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def dfs(node: 'Node'):
            if node is None:
                return
            # 前序遍历位置
            for ch in node.children:
                dfs(ch)
            # 后序遍历位置
            ans.append(node.val)
            
        dfs(root)
        return ans

