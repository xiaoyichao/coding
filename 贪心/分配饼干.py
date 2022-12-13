# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-07-21 21:47:13
LastEditTime: 2022-12-13 14:38:25
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。


Description: https://leetcode.cn/problems/assign-cookies/submissions/
这是一个分配问题
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


