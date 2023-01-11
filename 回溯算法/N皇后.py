# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-11 18:03:08
LastEditTime: 2023-01-11 18:04:28
Description: 
'''


def solveNQueens(n):
    def dfs(n, row, col, path):
        if row == n:
            res.append(path[:])
        for i in range(n):
            if col[i] == 'Q': continue
            if row - i == abs(col[i] - col[row]): continue
            if row + i == n - 1 - abs(col[i] - col[row]): continue
            col[i] = 'Q'
            n[row][i] = '.'
            dfs(n, row + 1, col, path + [n[row][:]])
            n[row][i] = '.'
            col[i] = 'Q'
    col, res = ['.' * n] * n, []
    dfs(n, 0, col, [])
    return res
n = 4
print(*solveNQueens(n))