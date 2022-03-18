# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: Please set LastEditors
Date: 2021-04-12 23:07:17
LastEditTime: 2022-03-18 11:51:06
Description: https://leetcode-cn.com/problems/valid-palindrome-ii/description/
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]: 
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True



s = Solution()
# 这个例子有问题
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
# print(s.validPalindrome("abcbfa"))
