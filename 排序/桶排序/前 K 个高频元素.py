
# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-11-14 17:34:52
LastEditTime: 2022-11-14 17:41:20
Description: 
https://leetcode.cn/problems/top-k-frequent-elements/description/
'''

from typing import List


class Solution:
   
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Author: xiaoyichao
        Description: 
        '''        
        bucket_range = set(nums)
        bucket_dict = {x:0 for x in bucket_range }
        for num in nums:
            v = bucket_dict[num]
            bucket_dict[num] = v+1
        a = sorted(bucket_dict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in a[:k] ]
