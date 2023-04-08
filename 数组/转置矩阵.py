"https://leetcode.cn/problems/transpose-matrix/?company_slug=jd"

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        # 初始化转置矩阵
        res = [[0] * m for _ in range(n)]
        # 遍历矩阵，将每个元素转移到转置矩阵中对应的位置
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res
