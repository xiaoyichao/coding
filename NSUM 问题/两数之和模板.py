'''
https://mp.weixin.qq.com/s/fSyJVvggxHq28a0SdmZm6Q

numbers 中可能有多对儿元素之和都等于 target，请你的算法返回所有和为 target 的元素对儿，其中不能出现重复。
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        numbers.sort()
        lo = 0
        hi = len(numbers)-1
        while lo < hi:
            two_sum = numbers[lo]+numbers[hi]
            left_num = numbers[lo]
            right_num = numbers[hi]
            if two_sum < target:
                while lo < hi and numbers[lo] == left_num:
                    lo += 1
            elif two_sum > target:
                while lo < hi and numbers[hi] == right_num:
                    hi -= 1
            elif two_sum == target:
                res.append([left_num, right_num])
                while lo < hi and numbers[lo] == left_num:
                    lo += 1
                while lo < hi and numbers[hi] == right_num:
                    hi -= 1
        return res

s= Solution()
res = s.twoSum([1, 3, 1, 2, 2, 3], 4)
print(res)

