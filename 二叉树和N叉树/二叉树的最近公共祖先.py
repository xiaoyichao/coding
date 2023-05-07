
"https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/"


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 情况 1
        if left and right:
            return root
        # 情况 2
        if not left and not right:
            return None
        # 情况 3
        return right if not left else left
        # return right if right else left
# 详细解析参见：
# https://labuladong.github.io/article/?qno=236
