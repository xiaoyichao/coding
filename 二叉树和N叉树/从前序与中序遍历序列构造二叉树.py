"https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?favorite=2cktkvj"

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 构造哈希映射，帮助我们快速定位根节点
        index = {val: i for i, val in enumerate(inorder)}
        
        # 递归函数
        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            # 若先序遍历和中序遍历范围为空，则退出递归
            # 在递归构建子树的过程中，我们需要不断缩小先序遍历和中序遍历的范围。当某一时刻先序遍历或中序遍历的范围为空时，说明当前子树已经构建完毕，这时候应该返回 None，退出当前递归
            if preorder_left > preorder_right or inorder_left > inorder_right:
                return None
            
            # 先序遍历的第一个节点是根节点
            root_val = preorder[preorder_left]
            root_index = index[root_val]
            
            # 创建当前子树的根节点
            root = TreeNode(root_val)
            
            # 递归构建左右子树
            # 注意划分左右子树的时候需要计算子树的大小
            left_size = root_index - inorder_left
            root.left = helper(preorder_left + 1, preorder_left + left_size, inorder_left, root_index - 1)
            root.right = helper(preorder_left + left_size + 1, preorder_right, root_index + 1, inorder_right)
            
            return root
        
        # 返回根节点
        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)


# labuladong
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 存储 inorder 中值到索引的映射
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1, valToIndex)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end, valToIndex):
        if pre_start > pre_end:
            return None

        # root 节点对应的值就是前序遍历数组的第一个元素
        root_val = preorder[pre_start]
        # root_val 在中序遍历数组中的索引
        index = valToIndex[root_val]

        left_size = index - in_start

        # 先构造出当前根节点
        root = TreeNode(root_val)

        # 递归构造左右子树
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, index - 1, valToIndex)

        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, index + 1, in_end, valToIndex)
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 存储 inorder 中值到索引的映射
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i

        return self.build(preorder, 0, len(preorder)-1,
                          inorder, 0, len(inorder)-1,
                          valToIndex)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end, valToIndex):
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        index = valToIndex[root_val]

        left_size = index - in_start

        root = TreeNode(root_val)

        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, index-1, valToIndex)
        root.right = self.build(preorder, pre_start+left_size+1, pre_end,
                                inorder, index+1, in_end, valToIndex)
        
        return root
