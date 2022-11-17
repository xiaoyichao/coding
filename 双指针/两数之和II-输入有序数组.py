# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2021-03-22 21:33:25
LastEditTime: 2021-03-25 22:11:44
Description: https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
'''


class Solution:
    """
    方向相反的双指针
    时间复杂度：O(n)，其中 n是数组的长度。两个指针移动的总次数最多为 n 次。

    空间复杂度：O(1)
    """    
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i <= j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum < target:
                i += 1
            else:
                j -= 1
        return[]


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
