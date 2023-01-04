# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-04 22:46:59
LastEditTime: 2023-01-04 22:47:00
Description: https://leetcode.cn/problems/reverse-string/
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j :
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s