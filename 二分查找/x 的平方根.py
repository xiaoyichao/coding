# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-08-02 01:10:44
LastEditTime: 2022-08-02 01:12:19
Description: https://leetcode.cn/problems/sqrtx/
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0,x//2+1, -1
        if x == 0:
            return 0
        while l<=r:
            middle = (l+r)//2
            
            if middle*middle <= x:
                l = middle + 1
                ans = middle
            else:
                r = middle - 1
        return ans
