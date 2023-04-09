"https://leetcode.cn/problems/kth-largest-element-in-an-array/"

import random
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 小顶堆，堆顶是最小元素
        pq = []
        for e in nums:
            # 每个元素都要过一遍二叉堆
            heapq.heappush(pq, e)
            # 堆中元素多于 k 个时，删除堆顶元素
            if len(pq) > k:
                heapq.heappop(pq)
        # pq 中剩下的是 nums 中 k 个最大元素，
        # 堆顶是最小的那个，即第 k 个最大元素
        return pq[0]
    

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 随机选择一个数作为枢纽元
        pivot = random.choice(nums)
        # 将原始列表分为三个子列表，分别存储小于、大于、等于枢纽元的数
        left = [x for x in nums if x < pivot]
        right = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]

        # 如果右边的列表的长度不小于k，说明第k大的数在右边列表中，递归查找右边列表
        if k <= len(right):
            return self.findKthLargest(right, k)
        # 如果右边列表长度加上等于枢纽元的列表长度仍小于k，则第k大的数在左边列表中，递归查找左边列表
        elif k > len(right) + len(mid):
            return self.findKthLargest(left, k - len(right) - len(mid))
        # 否则第k大的数就是枢纽元本身，直接返回
        else:
            return mid[0]








