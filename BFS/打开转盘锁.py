# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-27 15:09:10
LastEditTime: 2023-01-27 17:22:13
Description: https://leetcode.cn/problems/open-the-lock/

'''
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus_one(s, j):
            s = list(s)
            if s[j] == "9":
                s[j] = "0"
            else:
                s[j] = str(int(s[j]) + 1)
            return "".join(s)


        def minus_one(s, j):
            s = list(s)
            if s[j] == "0":
                s[j] = "9"
            else:
                s[j] = str(int(s[j]) - 1)
            return "".join(s)

        deads = set(deadends)
        visited = set()
        q = deque()
        step = 0
        q.append("0000")
        visited.add("0000")
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                # 判断是否达到终点
                if cur == target:
                    return step
                # 跳过不行的节点
                if cur in deads:
                    continue
                # 四位数，因此外层迭代是4
                for j in range(4):
                    # 每一位有两种情况
                    up = plus_one(cur,j)
                    down = minus_one(cur,j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1

        return -1

["0201","0101","0102","1212","2002"]
"0202"

s = Solution()
s.openLock(["0201", "0101", "0102", "1212", "2002"],
           "0202")

