"https://leetcode.cn/problems/3sum-closest/?company_slug=jd"

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        n = len(nums)
        
        for i in range(len(nums)):
            l, r = i+1, n-1
            while l<=r:
                sum = nums[i]+nums[l]+nums[r]
                if sum-target == 0:
                    return target
                elif sum-target<0:
                    l+=1
                    if abs(sum-target)<abs(diff):
                        diff= sum-target
                else:
                    r-=1
                    if abs(sum-target)<abs(diff):
                        diff= sum-target
        return diff+target
