"https://leetcode.cn/problems/house-robber-iii/"
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 这段代码是一种求解二叉树抢劫问题的动态规划算法，使用了备忘录技术来避免重复计算。

# 具体来说，该算法的思路是：

# 对于二叉树的每个节点，有两种选择：抢这个节点，或者不抢这个节点。

# 如果抢这个节点，那么就不能抢它的左右子节点，但可以抢它的左右子节点的子树，所以得到的价值应该是：该节点的值 + 左子节点的左右子树能抢到的最大价值 + 右子节点的左右子树能抢到的最大价值。

# 如果不抢这个节点，那么可以选择抢它的左右子节点，也可以选择不抢它的左右子节点，所以得到的价值应该是：左子节点的能抢到的最大价值 + 右子节点的能抢到的最大价值。

# 对于每个节点，分别计算选择抢或不抢的最大价值，并取两者的最大值作为该节点子树能抢到的最大价值。

# 使用备忘录技术避免重复计算，将每个节点的最大价值保存到一个 HashMap 中，下次如果遇到相同的节点就可以直接返回之前计算好的最大价值。

# 这种算法的时间复杂度是 O(N)，其中 N 是二叉树的节点数，空间复杂度也是 O(N)，因为需要使用 HashMap 来保存每个节点的最大价值。

class Solution:
    # 需要注意的是，Python 的字典类型是无序的，因此需要将 memo 定义为一个字典类型，而不是 HashMap。
    # 同时，Python 中没有 HashMap，可以使用字典类型来代替。此外，Python 中需要对 None 值进行特殊判断，因为它没有 Boolean 类型。
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return self.robSub(root, memo)

    def robSub(self, root, memo):
        if not root:
            return 0

        if root in memo:
            return memo[root]

        # 抢，然后去下下家
        do_it = root.val
        if root.left: #左节点的子树
            do_it += self.robSub(root.left.left, memo) + self.robSub(root.left.right, memo)
        if root.right: #右节点的子树
            do_it += self.robSub(root.right.left, memo) + self.robSub(root.right.right, memo)

        # 不抢，然后去下家（左右两节点）
        not_do = self.robSub(root.left, memo) + self.robSub(root.right, memo)

        res = max(do_it, not_do)
        memo[root] = res
        return res


# 这段代码是一个用动态规划算法求解二叉树抢劫问题的解法，代码主要实现了一个递归函数 dp，该函数接收一个二叉树的根节点，并返回一个大小为 2 的数组 arr。

# arr 数组的第一个元素表示如果不抢根节点 root 的钱，得到的最大收益；第二个元素表示如果抢了根节点 root 的钱，得到的最大收益。

# 首先判断根节点 root 是否为 None，如果是，则直接返回 [0, 0]。如果不是，则继续递归地调用 dp 函数，得到左子树和右子树的最大收益。然后根据抢或不抢根节点 root 来计算当前节点的最大收益。

# 具体地，如果抢了根节点 root，那么左子树和右子树就不能抢了，因此当前节点的最大收益为 root.val + left[0] + right[0]；如果不抢根节点 root，那么左子树和右子树就可以抢或不抢，因此当前节点的最大收益为 max(left[0], left[1]) + max(right[0], right[1])。

# 最后，返回 arr 数组即可。在 rob 函数中，调用 dp 函数求出根节点的最大收益，并返回 arr 数组的最大值作为整棵树的最大收益。

class Solution:
    # 需要注意的是，Python 中不需要显式地声明数组大小，因此可以直接定义数组，例如 return [0, 0] 表示返回一个大小为 2 的数组。
    # 同时，Python 中使用 max 函数来求最大值，可以直接传入多个参数进行比较，例如 max(left[0], left[1], right[0], right[1])。
    def rob(self, root: TreeNode) -> int:
        res = self.dp(root)
        return max(res[0], res[1])

    def dp(self, root):
        if not root:
            return [0, 0]
        left = self.dp(root.left)
        right = self.dp(root.right)
        # 抢，下家就不能抢了
        rob = root.val + left[0] + right[0]
        # 不抢，下家可抢可不抢，取决于收益大小
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return [not_rob, rob]
