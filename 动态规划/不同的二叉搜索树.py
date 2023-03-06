"https://leetcode.cn/problems/unique-binary-search-trees/?favorite=2cktkvj"

# 二叉搜索树（Binary Search Tree，BST）是一种特殊的二叉树，它满足以下性质：

# 若它的左子树不为空，则左子树上所有节点的值均小于根节点的值；
# 若它的右子树不为空，则右子树上所有节点的值均大于根节点的值；
# 它的左右子树也分别为二叉搜索树。
# 因此，二叉搜索树的中序遍历是升序排列的。这种数据结构可以快速地进行查找、插入、删除操作，时间复杂度为 O(log n)。

class Solution:
    def numTrees(self, n: int) -> int:
        # 处理特殊情况，当 n 为 0 或 1 时，只有一种情况
        if n == 0 or n == 1:
            return 1
        # 初始化动态规划数组，dp[i] 表示由 i 个节点组成的二叉搜索树的个数
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1  # 当只有 0 个或 1 个节点时，只有一种情况
        # 计算 dp[i] 的值
        for i in range(2, n+1):
            for j in range(1, i+1):
                # 将 j 作为根节点，左子树有 j-1 个节点，右子树有 i-j 个节点，
                # 则以 j 为根节点的二叉搜索树个数为 dp[j-1] * dp[i-j]
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]  # 返回由 n 个节点组成的二叉搜索树的个数
    

class Solution:
    def numTrees(self, n: int) -> int:
        # 定义count(start, end, memo)函数，表示以[start, end]之间的数构成的二叉搜索树的个数
        def count(start, end, memo):
            # 如果start>end，表示[start, end]之间没有数，构成的二叉搜索树只有一个空节点，返回1
            if start > end:
                return 1
            # 如果已经计算过以[start, end]之间的数构成的二叉搜索树的个数，直接返回结果
            if memo[start][end] != -1:
                return memo[start][end]
            # 定义变量res，用于存储以[start, end]之间的数构成的二叉搜索树的总数
            res = 0
            # 枚举[start, end]之间的每个数，将其作为根节点，递归计算左右子树的个数，并将左右子树的个数相乘，累加到res中
            for i in range(start, end+1):
                left = count(start, i-1, memo)  # 左子树的个数
                right = count(i+1, end, memo)  # 右子树的个数
                res += left * right  # 左右子树个数的乘积即为以i为根节点的二叉搜索树的个数，累加到res中
            # 将以[start, end]之间的数构成的二叉搜索树的总数记录到备忘录中
            memo[start][end] = res
            return res  # 返回以[start, end]之间的数构成的二叉搜索树的总数
        
        # 初始化备忘录，所有元素都为-1
        memo = [[-1] * (n+1) for _ in range(n+1)]
        # 返回1~n之间的数构成的二叉搜索树的总数
        return count(1, n, memo)




