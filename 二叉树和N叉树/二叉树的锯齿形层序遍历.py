"https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        flag=False
        while queue:
            level = []
            tmp_size = len(queue)
            for _ in range(tmp_size):
                cur_node = queue.popleft()

                level.append(cur_node.val)


                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            if flag is True:
                level.reverse()

            flag = not flag
            
            res.append(level)
        return res

