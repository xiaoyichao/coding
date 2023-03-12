"https://leetcode.cn/problems/course-schedule/?favorite=2cktkvj"

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化每门课程的入度和邻接表
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # 构建邻接表和入度列表
        for prerequisite in prerequisites:
            next_course, prev_course = prerequisite
            in_degree[next_course] += 1
            adj[prev_course].append(next_course)
        # 将所有入度为 0 的课程加入队列中
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        # 记录能够学完的课程数
        count = 0
        while queue:
            # 取出队列头部的课程
            course = queue.pop(0)
            count += 1
            # 遍历该课程的后继课程，将其入度减 1
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                # 如果该课程的入度为 0，将其加入队列
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        # 如果能够学完所有课程，返回 True，否则返回 False
        return count == numCourses
