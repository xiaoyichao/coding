'''
https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/2350660/huan-xing-zi-shu-zu-de-zui-da-he-by-leet-elou/

给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。

环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
'''
from typing import List


# 方法二：取反
# https://leetcode.cn/problems/maximum-sum-circular-subarray/


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        preMax, maxRes = nums[0], nums[0]
        preMin, minRes = nums[0], nums[0]
        sum_ = sum(nums)
        for i in range(1, n):
            preMax = max(preMax + nums[i], nums[i])
            maxRes = max(maxRes, preMax)
            preMin = min(preMin + nums[i], nums[i])
            minRes = min(minRes, preMin)
        if maxRes < 0: #说明数字中不包含大于等于0 的元素。minRes 将包括数组中的所有元素，导致我们实际取到的子数组为空。在这种情况下，我们只能取 maxRes 作为答案。
            return maxRes
        else:
            return max(maxRes, sum_ - minRes)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        left_max = [0] * n
        left_max[0] = nums[0]
        left_sum = nums[0]
        pre = nums[0]
        for i in range(1, n):
            pre = max(nums[i], pre+nums[i])
            res = max(res, pre)
            left_sum += nums[i]
            left_max[i] = max(left_max[i-1], left_sum)
        right_sum = 0
        for i in range(n-1, 0,-1):
            right_sum += nums[i]
            res = max(left_max[i-1]+right_sum, res)
        return res
