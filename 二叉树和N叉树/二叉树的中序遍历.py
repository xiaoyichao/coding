"https://leetcode.cn/problems/binary-tree-inorder-traversal/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        head = root
        def dfs(head):
            if not head:
                return
            dfs(head.left) #递归左子树
            res.append(head.val) # 添加当前节点的val 到res
            dfs(head.right) # 递归右子树

        dfs(head)
        return res
            
# 迭代
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 定义结果列表和辅助栈
        res = []
        stack = []
        # 定义当前节点指针，初始化为根节点
        cur = root
        # 循环遍历节点，直到节点为空且辅助栈也为空
        while cur or stack:
            # 如果当前节点不为空，将其入栈，并将当前节点移动到其左子节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 如果当前节点为空，说明已经到达最左边的叶子节点了，需要回溯到父节点
            else:
                # 从栈中弹出最后一个节点，并将其值添加到结果列表中
                node = stack.pop()
                res.append(node.val)
                # 将当前节点指针指向该节点的右子节点，继续遍历
                cur = node.right
        # 返回结果列表
        return res
