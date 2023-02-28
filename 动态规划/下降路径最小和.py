"https://leetcode.cn/problems/minimum-falling-path-sum/"

from typing import List
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

s= Solution()
res = s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(res)