"https://leetcode.cn/problems/two-sum/"

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 用字典存储每个元素的下标
        d = {}
        for i, num in enumerate(nums):
            # 查找是否存在一个对应的元素，使得这两个元素的和为目标值
            complement = target - num
            if complement in d:
                return [d[complement], i]
            # 如果找不到这样的元素，就将当前元素的下标加入字典
            d[num] = i
        # 如果整个数组都遍历完了，还是找不到符合条件的元素，就返回一个空数组
        return []
    