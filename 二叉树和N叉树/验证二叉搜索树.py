"https://leetcode.cn/problems/validate-binary-search-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 调用 check 函数，限定最小值和最大值为负无穷和正无穷
        return self.check(root, float('-inf'), float('inf'))
        
    def check(self, root, min_val, max_val):
        # 如果树为空，则是一棵二叉搜索树，返回 True
        if not root:
            return True
        
        # 如果当前节点值小于等于最小值或者大于等于最大值，则不是二叉搜索树，返回 False
        if root.val <= min_val or root.val >= max_val:
            return False
        
        # 递归检查左右子树，并限定其范围，左子树的范围为 (min_val, root.val)，右子树的范围为 (root.val, max_val)
        return self.check(root.left, min_val, root.val) and self.check(root.right, root.val, max_val)
