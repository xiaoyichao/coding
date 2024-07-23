"https://leetcode.cn/problems/number-of-islands/?favorite=2cktkvj"

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            # 如果越界或者当前格子是'0'，直接返回
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            # 将访问过的岛屿部分标记为'0'
            grid[i][j] = '0'
            # 继绺探索上下左右四个方向
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                # 当找到一个岛屿的新开始时
                if grid[i][j] == "1":
                    # 增加岛屿数量
                    res += 1
                    # 进行深度优先搜索来标记整个岛屿
                    dfs(grid, i, j)
        return res



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

