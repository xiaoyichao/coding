"https://leetcode.cn/problems/trapping-rain-water/"

from typing import List

class Solution:  
    # 这个解法的思路是，定义左右指针 left 和 right，以及左右最大高度 left_max 和 right_max，从左右两侧出发，每次比较左右两侧的高度，
    # 如果左侧小于右侧，则计算左侧的储水量，否则计算右侧的储水量。对于左右两侧，只需要维护当前的最大高度，即可计算储水量。
    # 时间复杂度为 $O(n)$，空间复杂度为 $O(1)$
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            # 更新左右边界的最大值
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 如果左边界的最大值小于右边界的最大值，则移动左边界
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            # 否则，移动右边界
            else:
                res += right_max - height[right]
                right -= 1
        
        return res
    
s = Solution()
res = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)
