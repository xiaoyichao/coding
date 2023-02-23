# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-04 22:59:05
LastEditTime: 2023-01-04 23:30:13
Description: https://leetcode.cn/problems/longest-palindromic-substring/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Palindrome(i, j, s):
            while i>=0 and j < len(s) and s[i] == s[j]:
                i-=1
            return s[i+1:j]
        res = ""
        for k in range(0,len(s)):
            # 找回文串的关键技巧是传入两个指针 l 和 r 向两边扩散，因为这样实现可以同时处理回文串长度为奇数和偶数的情况。
            res_l =  Palindrome(k,k,s)
            res_r = Palindrome(k,k+1,s)
            res = res_l if len(res_l) > len(res) else res
            res = res_r if len(res_r) > len(res) else res
        return res