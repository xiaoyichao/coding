"https://leetcode.cn/problems/house-robber/"
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
    # 这个递归会超时，真的很慢
        def dp(nums: List[int], start: int) -> int:
            if start >= len(nums):
                return 0
            # 状态就是当前的索引，选择就是是否抢这家
            res = max(
                # 不抢，去下家
                dp(nums, start + 1),
                # 抢，去下下家
                nums[start] + dp(nums, start + 2)
            )
            return res

        return dp(nums, 0)
    
    def rob(self, nums: List[int]) -> int:
    # 这个也会超时
        memo = [-1]*len(nums)
        # 返回 nums[start..] 能抢到的最大值
        def dp(nums: List[int], start: int) -> int:
            if start >= len(nums):
                return 0
            # 状态就是当前的索引，选择就是是否抢这家
            if memo[start] != -1:
                return memo[start]
            else:
                res = max(
                    # 不抢，去下家
                    dp(nums, start + 1),
                    # 抢，去下下家
                    nums[start] + dp(nums, start + 2)
                )
                return res
        return dp(nums, 0)
    
    def rob(self, nums: List[int]) -> int:
    # 能用迭代不要用递归，递归真的太慢了，慢到超乎你的想象
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_i_1 = 0
        dp_i_2 = 0
        dp_i = 0
        for i in range(n-1,-1,-1):
        # 遍历顺序是倒序的原因是，当前的dp_i的值取决于下一次循环中的dp_i_1和dp_i_2的值，分别是下一个和下下个循环中的值。通过倒序遍历，可以为每个循环计算出正确的dp_i_1和dp_i_2的值。
        # 如果我们从0到n-1循环，我们就需要使用先前循环中的dp_i_1和dp_i_2的值，而这些值在当前循环中还没有正确地更新，因此会导致错误的结果。
            dp_i = max(dp_i_1, nums[i]+dp_i_2)
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i
    

s = Solution()
# res = s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
res = s.rob([1,2,3,1])
print(res)
