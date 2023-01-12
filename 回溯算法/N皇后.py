# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-11 18:03:08
LastEditTime: 2023-01-12 18:31:32
Description: https:#leetcode.cn/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
'''
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n: # 停止的条件
                board = generateBoard()
                res.append(board)
            else:
                for i in range(n): 
                    #      列上有冲突     行与列之差 相等的不行       行与列之和 相等的不行
                    if i in columns or row - i in diagonal1 or row + i in diagonal2: #排除不合法选择
                        continue
                    queens[row] = i
                    #做选择
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)  #进入下一行决策
                    columns.remove(i)  #撤销选择
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        res = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return res

n = 4
s = Solution()
print(s.solveNQueens(n))

#下边这个解法，更符合labuladong的思路
def printQueen(): 
    print(queen)
    for i in range(8):
        for j in range(8):
            if queen[i][j]==1:
                print('☆ '*j+'★ '+'☆ '*(7-j))
    print("\n\n")
    
def check(row,column):
    # 检查行列
    for k in range(8):
        if queen[k][column]==1:
            return False 
    # 检查主对角线    
    for i,j in zip(range(row-1,-1,-1),range(column-1,-1,-1)):
        if queen[i][j]==1:
            return False   
    # 检查副对角线     
    for i,j in zip(range(row-1,-1,-1),range(column+1,8)):
        if queen[i][j]==1:
            return False          
    return True

def findQueen(row):
    if row>7:
        global count
        count+=1
        printQueen()
        return
    for column in range(8):
        if check(row,column):
            queen[row][column]=1
            findQueen(row+1)
            queen[row][column]=0

if __name__ == '__main__':
    count = 0
    queen = [[0 for i in range(8)] for i in range(8)] 
    findQueen(0)
    print("满足要求的摆法总数:", count)
