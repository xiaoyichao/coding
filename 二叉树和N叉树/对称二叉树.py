"https://leetcode.cn/problems/symmetric-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如果二叉树的根节点为空，则认为是轴对称的
        if not root:
            return True
        # 否则递归检查左子树和右子树是否轴对称
        return self.check(root.left, root.right)
    
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # 如果左子树和右子树都为空，则认为是轴对称的
        if not left and not right:
            return True
        # 如果左子树和右子树中只有一个为空，则认为不是轴对称的
        if not left or not right:
            return False
        # 如果左子树和右子树的根节点值不同，则认为不是轴对称的
        if left.val != right.val:
            return False
        # 递归检查左子树的左子树和右子树的右子树，以及左子树的右子树和右子树的左子树是否轴对称
        return self.check(left.left, right.right) and self.check(left.right, right.left)
