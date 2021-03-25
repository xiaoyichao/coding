# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2021-03-25 22:02:23
LastEditTime: 2021-03-25 22:29:37
Description: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
'''

import math


class Solution():
    """
    [时间复杂度O(sqrt(c))
    空间复杂度O(1)]
    """    
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            sum = i ** 2 + j ** 2
            if sum == c:
                return True
            elif sum < c:
                i += 1
            else:
                j -= 1
        return False


solution = Solution()
print(solution.judgeSquareSum(5))