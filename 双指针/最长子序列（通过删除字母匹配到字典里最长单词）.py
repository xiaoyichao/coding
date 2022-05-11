# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-16 10:25:14
LastEditTime: 2022-05-11 13:45:56
Description: 
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]

solution = Solution()
print(solution.findLongestWord(s, dictionary))
