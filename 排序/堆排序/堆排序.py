# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:11:28
LastEditTime: 2022-08-15 22:11:29
Description: 

前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


# 这一题的总体思路 总体时间复杂度 O(nlogk)O(nlogk)

# 遍历统计元素出现频率 O(n)O(n)
# 前k个数构造 规模为 k+1 的最小堆 minheap， O(k)O(k)， 注意 +1 是因为占位节点。
# 遍历规模k之外的数据，大于堆顶则入堆，下沉维护规模为k的最小堆 minheap. O(nlogk)O(nlogk)
# (如需按频率输出，对规模为k的堆进行排序)

# 作者：xxinjiee
# 链接：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/python-dui-pai-xu-by-xxinjiee/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1) 
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1) 
        return [item[0] for item in heap[1:]]

s = Solution()
alist = s.topKFrequent([1,1,1,2,2,3],2)
print(alist)

