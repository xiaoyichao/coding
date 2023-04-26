# coding=UTF-8
'''
https://leetcode.cn/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict= {}
        for i in range(len(nums)):
            c = target-nums[i]
            if c in num_dict:
                return [i, num_dict[c]]
            else:
                num_dict[nums[i]] = i
        return []


                
                    
            
s = Solution()
result = s.twoSum([1,2,3,5,7], 9)
print(result)