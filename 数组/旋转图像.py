"https://leetcode.cn/problems/rotate-image/?favorite=2cktkvj"

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1] 
            # 这里使用了 Python 中的切片（slicing）语法，其中 [::-1] 表示从后往前以步长为-1的方式遍历整个数组，即将数组反转。
        # 或者这样，第二个循环不用切片的操作，但是用切片更好
        for i in range(n+1):
            for j in range(n//2+1):
                matrix[i][j], matrix[i][n-j] = matrix[i][n-j], matrix[i][j]