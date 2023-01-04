# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-04 22:58:11
LastEditTime: 2023-01-04 22:58:12
Description: https://leetcode.cn/problems/valid-palindrome/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(ch.lower() for ch in s if ch.isalnum())
        print(s)
        l = 0 
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
        return True