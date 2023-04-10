"https://leetcode.cn/problems/house-robber-ii/"
from typing import List


class Solution:
    # 首先，首尾房间不能同时被抢，那么只可能有三种不同情况：要么首尾两个房间都不被抢；要么第一间房子被抢最后一间不抢；要么最后一间房子被抢第一间不抢。
    # 这三种情况，哪种的结果最大，就是最终答案呗！不过，其实我们不需要比较三种情况，只要比较情况二和情况三就行了，
    # 因为这两种情况对于房子的选择余地比情况一大呀，房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小。
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def rob_range(start,end,nums):
            dp_i_1 = 0
            dp_i_2 = 0
            dp_i = 0
            for i in range(end, start-1, -1):
                dp_i = max(dp_i_1, nums[i]+dp_i_2)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i

        if n<=1:
            return 0
        else:
            return max(rob_range(0,n-2,nums), rob_range(1,n-1,nums))
    

s = Solution()
# res = s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
res = s.rob([1,2,3,1])
print(res)
