# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-13 15:38:18
LastEditTime: 2022-12-13 16:52:39
Description: 

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk+1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, len(occ))  # len(occ) 是现在的结果。
            # ans = max(ans, rk - i + 1)  # （rk - i + 1）是现在的结果。ans在max计算之前是从前的结果。
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:

        occ = set()
        n = len(s)
        ans = 0
        rk = -1
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
            # while s[rk+1] not in occ and rk+1 < n:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, len(occ))
            # ans = max(ans, rk - i + 1)
        return ans

s = Solution()
ans = s.lengthOfLongestSubstring("abcabcbb")
print(ans)
