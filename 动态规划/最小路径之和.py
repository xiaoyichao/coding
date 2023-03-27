"""
这个题目是二维动态规划的题目
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
https://leetcode-cn.com/problems/minimum-path-sum/

时间复杂度：O(mn)，其中 m 和 n 分别是网格的行数和列数。需要对整个网格遍历一次，计算dp 的每个元素的值。

空间复杂度：O(mn)，其中 m 和 n 分别是网格的行数和列数。创建一个二维数组dp，和网格大小相同。
空间复杂度可以优化，例如每次只存储上一行的dp 值，则可以将空间复杂度优化到 O(n)


"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]  # 构造缓存
        # dp = [[0] * columns] * rows  这句有问题，因为列表是指针到内存的。
        dp[0][0] = grid[0][0]  # 初始化左上角数据
        # 一共三个情况
        for i in range(1, rows):  # 第一列的数据，只能从第一列的左侧往右移动
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):  # 第一行的数据，只能在第一行从上往下移动
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):  # 不是第一行也不是第一列的数据，从左侧或者上侧移动而来
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

    def minPathSum_1(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0] * rows] * columns
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


# 空间复杂度可以优化，例如每次只存储上一行的dp 值，则可以将空间复杂度优化到 O(n)
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if i == j == 0: continue
#                 elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
#                 elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
#                 else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
#         return grid[-1][-1]



s= Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
res = s.minPathSum(grid)
print(res)
