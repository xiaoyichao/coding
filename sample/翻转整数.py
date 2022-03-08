# coding=UTF-8
'''
Author: 
LastEditors: Please set LastEditors
Date: 2022-03-08 21:17:32
LastEditTime: 2022-03-08 21:29:11
Description: 
'''
class Solution:
    def reverse_(self, x: int) -> int:
        s=str(x)[::-1].rstrip('-')
        if int(s)<2**31:
            if x>=0:
                return int(s)
            else:
                return 0-int(s)
        return 0
    
s = Solution()
r = s.reverse_(-123)
print(r)