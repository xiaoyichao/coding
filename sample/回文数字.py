# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-08 21:50:49
LastEditTime: 2022-03-08 21:51:52
Description: 
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)[::-1]
        if str(x)==y:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(121))
