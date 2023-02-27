"https://leetcode.cn/problems/minimum-falling-path-sum/"

from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mem = [[float("inf")]* len(matrix[0]) for i in range(len(matrix))]
        # print(mem)
        res = float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = min(res, self.dp(i,j,mem, matrix))
        return mem[i,j]

    def dp(self, i, j, mem, matrix):
        if i == 0:
            mem[i][j] = matrix[i][j]
        if mem[i][j] != float("-inf"):
            return mem[i][j]
        print(i,j, mem[i][j], matrix[i][j])
        mem[i][j] = matrix[i][j] + min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
        return mem[i][j]

s= Solution()
res = s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(res)