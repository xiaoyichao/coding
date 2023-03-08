"https://leetcode.cn/problems/maximum-product-subarray/?favorite=2cktkvj"

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # 定义两个数组f_max和f_min，分别表示以当前位置为结尾的乘积最大值和乘积最小值
        f_max = [0] * n
        f_min = [0] * n
        # 初始化，以第一个数为结尾的子数组中最大值和最小值都是第一个数本身
        f_max[0] = nums[0]
        f_min[0] = nums[0]
        # 遍历数组，逐个计算f_max和f_min数组的值
        for i in range(1, n):
            if nums[i] > 0:
                 # 如果当前数是非负数，那么乘以以前的最大值会变成最大值，乘以以前的最小值会变成最小值
                f_max[i] = max(nums[i], f_max[i-1] * nums[i])
                f_min[i] = min(nums[i], f_min[i-1] * nums[i])
            # 如果当前数是负数，那么乘以以前的最小值会变成最大值，乘以以前的最大值会变成最小值
            else:
                f_max[i] = max(nums[i], f_min[i-1] * nums[i])
                f_min[i] = min(nums[i], f_max[i-1] * nums[i])
        # 返回f_max数组中的最大值即可
        return max(f_max)
