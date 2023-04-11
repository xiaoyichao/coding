"https://leetcode.cn/problems/minimum-falling-path-sum/"

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 初始化dp数组
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        # 动态规划求解
        for i in range(1, n):
            for j in range(n):
                # 边界情况：上一行第一个元素或最后一个元素
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        # 取最小值
        return min(dp[-1])


s= Solution()
res = s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(res)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mem = [[float("inf")]* len(matrix[0]) for i in range(len(matrix))]
        res = float("inf")
        for j in range(len(matrix)):
            res = min(res, self.dp(n-1, j, mem, matrix ))
        return res

    def dp(self, i, j, mem, matrix ):
        # base case
        if i == 0:
            return matrix[0][j]
        # 查找备忘录
        if mem[i][j] != float("inf"):
            return mem[i][j]
        # 进行状态转移
        left = self.dp(i-1,j-1, mem, matrix) if j-1>=0 else float("inf") 
        mid = self.dp(i-1,j, mem, matrix)
        right = self.dp(i-1,j+1, mem, matrix) if j+1<len(matrix[0]) else float("inf")
        mem[i][j] = matrix[i][j] + min(left,
                                       mid,
                                       right)
        return mem[i][j]
