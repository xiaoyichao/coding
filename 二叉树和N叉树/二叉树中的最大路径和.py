"https://leetcode.cn/problems/binary-tree-maximum-path-sum/"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # 递归计算左右子节点的最大贡献值，我们取 max(max_gain(node.left), 0)，这样如果左子树的贡献值为负，就直接取0，也就是说，我们选择不包括左子树的路径。
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 当前节点的最大路径和
            current_path_sum = node.val + left_gain + right_gain
            
            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 返回节点的最大贡献值
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')  # 全局变量，表示所有路径中的最大值
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node: TreeNode) -> int:
        """本质上是个后续遍历

        Args:
            node (TreeNode): [description]

        Returns:
            int: [description]
        """        
        if not node:
            return 0
        
        # 计算左右子树经过该节点的最大路径和
        left = max(self.max_gain(node.left), 0)
        right = max(self.max_gain(node.right), 0)
        
        # 计算包含该节点的最大路径和，更新全局变量max_sum
        cur_sum = node.val + left + right
        self.max_sum = max(self.max_sum, cur_sum)
        
        # 返回包含当前节点的最大路径和
        return node.val + max(left, right)
