
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
import heapq
from collections import Counter

class Solution:
    # 堆排序的思想
    def topKFrequent(nums, k):
        # 统计每个元素出现的频率
        counter = Counter(nums)
        # 构建最小堆
        heap = []
        for num, freq in counter.items():
            # 堆未满时直接插入
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                # 如果堆已满，比较堆顶元素和当前元素的频率
                # 如果当前元素的频率大于堆顶元素的频率，弹出堆顶元素，插入当前元素
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        # 将堆中元素转换为列表返回
        res = [num for freq, num in heap]
        return res



    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Author: xiaoyichao
        Description: 桶排序的思想
        '''        
        bucket_range = set(nums)
        bucket_dict = {x:0 for x in bucket_range }
        for num in nums:
            v = bucket_dict[num]
            bucket_dict[num] = v+1
        a = sorted(bucket_dict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in a[:k] ]
