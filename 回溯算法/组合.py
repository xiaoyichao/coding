# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-23 13:41:28
LastEditTime: 2023-01-23 17:12:43
Description: https://leetcode.cn/problems/combinations/

组合（元素无重不可复选）
'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []

        def backtrack(satrt, n, k):
            if k == len(track):  # base case
                # 遍历到了第 k 层，收集当前节点的值
                res.append(track[:])
                return
            # 回溯算法标准框架
            for i in range(satrt, n+1):
                # 选择
                track.append(i)
                # 通过 start 参数控制树枝的遍历，避免产生重复的子集
                backtrack(i+1, n, k)
                # 撤销选择
                track.pop()
        backtrack(1, n, k)
        return res

s =Solution()
s.combine(4,2)
