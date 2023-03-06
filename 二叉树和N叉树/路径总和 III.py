# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-19 15:42:04
LastEditTime: 2022-12-19 17:54:50
Description: https://leetcode.cn/problems/path-sum-iii/solution/lu-jing-zong-he-iii-by-leetcode-solution-z9td/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: #路径总和3 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: # 深度优先搜索
        def rootsum(root, targetSum):
            if root is None:
                return 0
            ret = 0
            if root.val == targetSum:
                ret += 1
            ret += rootsum(root.left, targetSum - root.val)
            ret += rootsum(root.right, targetSum - root.val)
            return ret

        if root is None:    
            return 0
        ret = rootsum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret
            
