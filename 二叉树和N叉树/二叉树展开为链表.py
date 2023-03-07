"https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1、将 root 的左子树和右子树拉平。
    # 2、将 root 的右子树接到左子树下方，然后将整个左子树作为右子树。
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root:
            return
        
        # 先递归拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 后序遍历位置
        # 1、左右子树已经被拉平成一条链表
        left = root.left
        right = root.right
        
        # 2、将左子树作为右子树
        root.left = None
        root.right = left
        
        # 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right

