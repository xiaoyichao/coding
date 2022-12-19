# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-19 15:42:04
LastEditTime: 2022-12-19 15:44:05
Description: 
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: #路径总和3
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        res = 0
                
        def dfs(root,targetSum,path):
            if not root:        

                return     
            path.append(root.val)   

            if not root.left and not root.right and sum(path) == targetSum:

                res += 1
                    
            dfs(root.left,targetSum,path)

            
            dfs(root.right,targetSum,path)

            path.pop()

        dfs(root,targetSum,[])
        

        return res



            

