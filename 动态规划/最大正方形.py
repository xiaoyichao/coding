"https://leetcode.cn/problems/maximal-square/"

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # 初始化dp
        dp = [ [0]*n for _ in range(m)]
        # base case
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        # 状态转移
        for i in range(1,m):
            for j in range(j,n):
                if matrix[i][j]== str(0):
                    continue
                dp[i][j] =  min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dp[i][j])
    
        return max_len**2