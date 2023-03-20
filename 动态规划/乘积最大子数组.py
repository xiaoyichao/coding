"https://leetcode.cn/problems/maximum-product-subarray/?favorite=2cktkvj"

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # 定义：以 nums[i] 结尾的子数组，乘积最小为 dp1[i]
        dp1 = [0] * n
        # 定义：以 nums[i] 结尾的子数组，乘积最大为 dp2[i]
        dp2 = [0] * n

        # base case
        dp1[0] = nums[0]
        dp2[0] = nums[0]

        # 状态转移方程
        for i in range(1, n):
            dp1[i] = min(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])
            dp2[i] = max(dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i])

        # 遍历所有子数组的最大乘积，求最大值
        res = max(dp2)

        return res
    
# 更好的方法，只保留最近的结果，
# 在更新dp_min和dp_max时，应该在同一轮循环内先更新dp_min，再更新dp_max，因为更新dp_max时需要用到dp_min的值，
# 如果先更新dp_max，那么dp_min的值就已经被更新过了，不是原始的dp_min的值了。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_min = nums[0]
        dp_max = nums[0]
        res = dp_max
        for i in range(1, n):
            prev_dp_min = dp_min
            dp_min = min(prev_dp_min * nums[i], dp_max * nums[i], nums[i])
            dp_max = max(prev_dp_min * nums[i], dp_max * nums[i], nums[i])
            res = max(res, dp_max)
        return res