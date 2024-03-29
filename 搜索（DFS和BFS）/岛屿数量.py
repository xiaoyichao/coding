"https://leetcode.cn/problems/number-of-islands/?favorite=2cktkvj"

from typing import List


# 这个代码很精简啊
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 计算岛屿数量的函数
        def dfs(grid, i, j):
            # 若行或列超出边界，或者遇到水，则返回0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0

            # 将访问过的陆地标记为0
            grid[i][j] = '0'

            # 继续递归搜索上下左右四个方向
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

            return 1

        # 初始化岛屿数量为0
        num_of_islands = 0

        # 遍历网格中的所有元素
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果当前元素是陆地，岛屿数量加1，并执行深度优先搜索
                if grid[i][j] == '1':
                    num_of_islands += dfs(grid, i, j)

        return num_of_islands



# labuladong
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        # 遍历 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 每发现一个岛屿，岛屿数量加一
                    res += 1
                    # 然后使用 DFS 将岛屿淹了
                    self.dfs(grid, i, j)
        return res

    # 从 (i, j) 开始，将与之相邻的陆地都变成海水
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引边界
            return
        if grid[i][j] == '0':
            # 已经是海水了
            return
        # 将 (i, j) 变成海水
        grid[i][j] = '0'
        # 淹没上下左右的陆地
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)

