"https://leetcode.cn/problems/binary-tree-maximum-path-sum/"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')  # 全局变量，表示所有路径中的最大值
        self.helper(root)
        return self.max_sum

    def helper(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        # 计算左右子树经过该节点的最大路径和
        left = max(self.helper(node.left), 0)
        right = max(self.helper(node.right), 0)
        
        # 计算包含该节点的最大路径和，更新全局变量max_sum
        cur_sum = node.val + left + right
        self.max_sum = max(self.max_sum, cur_sum)
        
        # 返回包含当前节点的最大路径和
        return node.val + max(left, right)
