# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-04 22:59:05
LastEditTime: 2023-01-04 23:30:13
Description: https://leetcode.cn/problems/longest-palindromic-substring/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str: # 双指针的方式，中心扩展法
        n = len(s)
        if n < 2:
            return s

        # 定义判断回文串的函数，输入为起始指针 i 和 j，字符串 s
        # 如果 i 和 j 相等，向两边扩散查找，直到不是回文串为止
        def Palindrome(i, j, s):
            while i>=0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
            # 当找到回文子串时，i 指向左侧的回文子串的第一个字符的左边，而 j 指向右侧回文子串的第一个字符的右边。
            # 因此，当返回回文子串时，索引位置都得还原一次，这两个 i+=1，j-=1 操作之后，i, j才是起始位置。[]的右边取不到，所以返回的时候j还得+1
            i+=1
            j-=1
            return s[i: j+1]
        
        res = ""
        for k in range(0,len(s)):
            # 找回文串的关键技巧是传入两个指针 l 和 r 向两边扩散，因为这样实现可以同时处理回文串长度为奇数和偶数的情况。
            res_l =  Palindrome(k,k,s)
            res_r = Palindrome(k,k+1,s)
            res = res_l if len(res_l) > len(res) else res
            res = res_r if len(res_r) > len(res) else res
        return res
    
class Solution: #动态规划的方式
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(res):
                    res = s[i:j + 1]
        return res
