# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-19 15:42:04
LastEditTime: 2022-12-19 17:54:50
Description: https://leetcode.cn/problems/path-sum-iii/solution/lu-jing-zong-he-iii-by-leetcode-solution-z9td/
'''
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前缀和
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            res = 0
            curr += root.val
            res += prefix[curr - targetSum]
            prefix[curr] += 1
            res += dfs(root.left, curr)
            res += dfs(root.right, curr)
            prefix[curr] -= 1

            return res

        return dfs(root, 0)

def pathSum(root, targetSum):
    def dfs(node, curr_sum):
        nonlocal count
        if not node:
            return
        
        curr_sum += node.val
        
        # Check if there is a sub-path (ending at this node) that sums to target
        if curr_sum - targetSum in prefix_sum:
            count += prefix_sum[curr_sum - targetSum]
        
        # Update the prefix sums with the current sum
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        # Recurse on the left and right children
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        
        # Remove the current sum from the prefix sums to backtrack
        prefix_sum[curr_sum] -= 1
        if prefix_sum[curr_sum] == 0:
            del prefix_sum[curr_sum]
    
    count = 0
    prefix_sum = {0: 1}  # Initialize prefix_sum with base case
    dfs(root, 0)
    return count

class Solution: #路径总和3 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: # 深度优先搜索
        def rootsum(root, targetSum):
            if root is None:
                return 0
            res = 0
            if root.val == targetSum:
                res += 1
            res += rootsum(root.left, targetSum - root.val)
            res += rootsum(root.right, targetSum - root.val)
            return res

        if root is None:    
            return 0
        res = rootsum(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res
            
