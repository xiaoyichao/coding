"https://leetcode.cn/problems/maximal-square/"
'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # 初始化dp
        dp = [ [0]*n for _ in range(m)]
        # 基本情况初始化
        for i in range(m):
            # 传过来的是str
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        # 状态转移
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == str(0):
                    continue
                # 新的正方形的边长取决于它的左边、上边和左上角三个位置的最小值。
                dp[i][j] =  min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dp[i][j])
    
        return max_len**2
