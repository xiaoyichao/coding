# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-18 11:51:45
LastEditTime: 2022-03-18 13:13:31
Description: 
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/

'''

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]: 
                    # 判断是否有子串
                    i += 1
                j += 1
            if i == len(t):
                # 更新的条件
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res


s = Solution()
print(s.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
