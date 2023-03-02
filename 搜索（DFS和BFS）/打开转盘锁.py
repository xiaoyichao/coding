# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-27 15:09:10
LastEditTime: 2023-01-27 19:04:50
Description: https://leetcode.cn/problems/open-the-lock/

'''
from typing import List
from collections import deque


class Solution:
    # 单向BFS
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


class Solution:
    # 双向BFS,这段代码有问题，没有得到想要的结果
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
        q_1 = set()
        q_2 = set()
        step = 0
        q_1.add("0000")
        q_2.add(target)
        # visited.add("0000")
        while q_1 and q_2:
            temp = set()
            for cur in q_1:
                # 判断是否达到终点,也就是Q1和2连上了。
                if cur in q_2:
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
                        temp.add(up)
                        visited.add(up)
                    if down not in visited:
                        temp.add(down)
                        visited.add(down)
            step += 1
            # temp 相当于 q1, 这里交换 q1 q2，下一轮 while 就是扩散 q2
            q_1 = q_2
            q_2 = temp

        return -1



s = Solution()
s.openLock(["0201", "0101", "0102", "1212", "2002"],
           "0202")
