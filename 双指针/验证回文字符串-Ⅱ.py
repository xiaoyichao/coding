# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2021-04-12 23:07:17
LastEditTime: 2021-04-13 00:05:57
Description: https://leetcode-cn.com/problems/valid-palindrome-ii/description/
'''


class Solution:
    def validPalindrome(self, s: str):
        s = list(s)
        i = 0
        j = len(s) - 1
        del_num = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i+1] == s[j]:
                i += 1
                del_num += 1
            elif s[i] == s[j-1]:
                j -= 1
                del_num += 1
            else:
                print("doubuxing",s[i], s[j], s[i+1], s[j], s[i],s[j-1],i,j )
                return False
            if del_num > 1:
                return False
        return True


s = Solution()
# 这个例子有问题
# print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
print(s.validPalindrome("abcbfa"))
