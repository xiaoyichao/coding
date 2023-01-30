# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-30 13:30:51
LastEditTime: 2023-01-30 14:42:55
Description: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
'''

from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        r = 0
        valid = 0
        need = defaultdict(int)
        window = defaultdict(int)
        res = []
        
        for x in p:
            need[x] += 1

        while(r<len(s)):
        
            c = s[r]
            r+=1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid+=1

            while(r-l==len(p)):
                if valid == len(need):
                    res.append(l)
                
                d = s[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -= 1
                
        return res


# 这个是for循环写的，尽量别看
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        valid = 0
        need = defaultdict(int)
        window = defaultdict(int)
        res = []
        
        for x in p:
            need[x] += 1

        for r in range(len(s)):
            c = s[r]
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid+=1

            while(r-l+1==len(p)):
                if valid == len(need):
                    res.append(l)
                
                d = s[l]
                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -= 1
                l += 1
                   

        return res

s = Solution()
res = s.findAnagrams("cbaebabacd", "abc")
