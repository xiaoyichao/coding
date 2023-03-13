"https://leetcode.cn/problems/course-schedule/?favorite=2cktkvj"

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 记录一次 traverse 递归经过的节点
        onPath = [False] * numCourses
        # 记录遍历过的节点，防止走回头路
        visited = [False] * numCourses
        # 记录图中是否有环
        hasCycle = [False]

        graph = self.buildGraph(numCourses, prerequisites)

        def traverse(s):
            if onPath[s]:
                # 出现环
                hasCycle[0] = True 
            if visited[s] or hasCycle[0]:
                # 如果已经找到了环，也不用再遍历了
                return
            # 前序遍历代码位置
            visited[s] = True
            onPath[s] = True
            for t in graph[s]:
                traverse(t)
            # 后序遍历代码位置
            onPath[s] = False
        
        for i in range(numCourses):
            # 遍历图中的所有节点
            traverse(i)
        
        # 只要没有循环依赖可以完成所有课程
        return not hasCycle[0]
    
    def buildGraph(self, numCourses, prerequisites):
        # 图中共有 numCourses 个节点
        graph = [[] for _ in range(numCourses)]
        for from_, to in prerequisites:
            # 修完课程 from_ 才能修课程 to
            # 在图中添加一条从 from_ 指向 to 的有向边
            graph[from_].append(to)
        return graph


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
