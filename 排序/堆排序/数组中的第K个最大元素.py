"https://leetcode.cn/problems/kth-largest-element-in-an-array/"

import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int) -> int:
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]
            pivot = left
            for i in range(left, right):
                if nums[i] > nums[right]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1
            nums[pivot], nums[right] = nums[right], nums[pivot]
            return pivot

        def quick_select(left: int, right: int, k: int) -> int:
            if left == right:
                return nums[left]
            pivot = partition(left, right)
            if k == pivot:
                return nums[k]
            elif k < pivot:
                return quick_select(left, pivot - 1, k)
            else:
                return quick_select(pivot + 1, right, k)

        return quick_select(0, len(nums) - 1, k - 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()
        nums.reverse()
        num = nums[k-1]
        return num



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

