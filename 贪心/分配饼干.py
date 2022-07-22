# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-07-21 21:47:13
LastEditTime: 2022-07-21 21:49:01
Description: https://leetcode.cn/problems/assign-cookies/submissions/
'''

from typing import List


class Solution():
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        len_g = len(g)
        len_s = len(s)
        while i < len_g and j < len_s:
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i
