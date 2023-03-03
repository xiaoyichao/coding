"https://leetcode.cn/problems/word-search/?favorite=2cktkvj"

from typing import List

class Solution: # 外边是回溯，里边是DFS
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 定义 DFS 函数
        def dfs(i, j, k):
            # 判断当前格子是否越界或当前字符是否与单词中对应字符匹配
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            # 如果已经匹配到了单词的末尾字符，则返回 True
            if k == len(word) - 1:
                return True
            # 用占位符标记当前格子已访问
            temp, board[i][j] = board[i][j], '/'
            # 递归搜索相邻的格子
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # 恢复当前格子的状态
            board[i][j] = temp
            # 返回结果
            return res
        
        # 遍历整个网格，对每个格子调用 DFS 函数
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    # 如果找到了单词，则返回 True
                    return True
        
        # 如果遍历整个网格后仍然没有找到单词，则返回 False
        return False
