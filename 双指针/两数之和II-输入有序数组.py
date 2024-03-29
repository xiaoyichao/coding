# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao xiao_yi_chao@163.com
Date: 2021-03-22 21:33:25
LastEditTime: 2023-02-25 21:45:32
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

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        res = []
        while left< right:
            if numbers[left] + numbers[right]== target:
                res = [left+1, right+1]
                return res
            elif numbers[left] + numbers[right] < target:
                left+=1
            else:
                right-=1
        return res
        

solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
