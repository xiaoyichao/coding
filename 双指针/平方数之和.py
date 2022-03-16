# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: Please set LastEditors
Date: 2021-03-25 22:02:23
LastEditTime: 2022-03-15 09:18:48
Description: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
'''

import math


class Solution():
    """
    [时间复杂度O(sqrt(c))
    空间复杂度O(1)]
    """    
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(pow(c, 0.5))
        while i<=j:
            sum_num = i**2 + j**2
            if sum_num == c:
                return True
            elif sum_num < c:
                i+=1
            else:
                j-=1
        return False


solution = Solution()
print(solution.judgeSquareSum(5))