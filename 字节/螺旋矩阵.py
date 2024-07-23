'''
https://leetcode.cn/problems/spiral-matrix/
这种题目就是纯模拟了
'''
from typing import List

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 如果矩阵为空，则返回空列表
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        # 获取矩阵的行数和列数
        rows, columns = len(matrix), len(matrix[0])
        # 定义四个方向：右，下，左，上
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # 总的元素数量
        total = rows * columns
        # 初始化一个同样大小的矩阵用于标记已经访问过的元素
        used = [[False] * columns for _ in range(rows)]
        # 初始化结果数组
        res = [0] * total
        # 当前方向索引
        dir = 0
        # 起始位置
        row, col = 0, 0

        for i in range(total):
            # 将当前元素加入结果数组
            res[i] = matrix[row][col]
            # 标记当前元素为已访问
            used[row][col] = True
            # 计算下一个位置
            new_row = row + dirs[dir][0]
            new_col = col + dirs[dir][1]
            # 检查下一个位置是否在界内且未被访问过
            if not (0 <= new_row < rows and 0 <= new_col < columns and not used[new_row][new_col]):
                # 如果不满足条件，改变方向
                dir = (dir + 1) % 4
                # 重新计算下一个位置
                new_row = row + dirs[dir][0]
                new_col = col + dirs[dir][1]
            # 更新当前行和列
            row, col = new_row, new_col

        return res