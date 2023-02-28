# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-02-28 18:09:30
LastEditTime: 2023-02-28 18:37:05
Description: https://leetcode.cn/problems/generate-parentheses/
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        track = ""  # 回溯过程中的路径
        self.backtrack(n, n, track, res)  # 可用的左括号和右括号数量初始化为 n
        return res

    def backtrack(self, left: int, right: int, track: str, res: List[str]):
        #可用的左括号数量为 left 个，可用的右括号数量为 rgiht 个
        if right < left:  # 若左括号剩下的多，说明不合法
            return
        if left < 0 or right < 0:  # 数量小于 0 肯定是不合法的
            return
        if left == 0 and right == 0:  # 当所有括号都恰好用完时，得到一个合法的括号组合, 触发结束条件
            res.append(track)
            return

        # 尝试放一个左括号
        track += "("
        self.backtrack(left - 1, right, track, res)
        track = track[:-1]

        # 尝试放一个右括号
        track += ")"
        self.backtrack(left, right - 1, track, res)
        track = track[:-1]



class Solution: # DFS的解法 
    # 在搜索的过程中，我们先判断左括号是否还有剩余，如果有，则可以在当前组合后加上左括号；如果没有了，则不能加左括号。
    # 接着，我们再判断右括号是否还有剩余，如果有，则可以在当前组合后加上右括号；但要注意的是，加上右括号的前提条件是当前组合中已经有左括号，否则加上右括号后不再是一个有效的组合。
    # 最终，当 left 和 right 都为零时，表示已经生成了一个有效的括号组合，将其添加到 res 中即可。最后，返回所有有效的括号组合。
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, "", res)
        return res
        
    def dfs(self, left: int, right: int, path: str, res: List[str]):
        if left == 0 and right == 0:
            res.append(path)
            return
        
        if left > 0:
            self.dfs(left - 1, right, path + "(", res)
        
        if right > left:
            self.dfs(left, right - 1, path + ")", res)
