# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-08-15 22:03:53
LastEditTime: 2022-12-13 13:57:36
Description:

https://leetcode.cn/problems/sort-an-array/submissions/

一句话总结：快速排序是先将一个元素排好序（左边不比这个元素大，右边比这个元素大），然后再将剩下的元素排好序。
快速排序算法其实很简单，采用分治策略。步骤如下：

选取一个基准元素（pivot）
比pivot小的放到pivot左边，比pivot大的放到pivot右边
对pivot左边的序列和右边的序列分别递归的执行步骤1和步骤2

快速排序就是一个二叉树的前序遍历，你甚至将快速排序的过程看成一个构造二叉搜索树（左子树的元素都比根节点元素小，右子树的元素都比根节点元素大）的过程。
但是这个时候，也会可能出现二叉树不均衡的情况（变成单链表的形式），这个时候就需要引入随机化的思想，随机选取一个元素作为pivot，这样就可以避免二叉树不均衡的情况。

平均的时间复杂度和归并排序一样是O(NlogN), 极限的情况下，数据都在某一侧，那么就树的深度就会变成N,时间复杂度就会变成O(N^2)

快速排序也是用到了分治思想和递归实现方式，这一点跟归并排序是一样的，但是快速排序的实现跟归并是完全不一样的。
归并排序是先分解再合并，从下到上解决问题。
快速排序是从上到下进行分区实现排序。


快速排序是一种不稳定排序算法，主要原因在于在排序过程中涉及到元素的交换操作，这会导致相等元素在序列中的相对位置发生变化。例如，在快速排序过程中，如果存在两个相等元素A和B，并且A在B之前，那么在排序过程中，可能会将B移到A的前面，从而导致它们的相对位置发生变化，这就破坏了稳定性。
相反，归并排序是一种稳定排序算法，因为在归并排序中，只涉及到元素的比较操作，不涉及到元素的交换操作，因此相等元素的相对位置不会发生变化，保持了稳定性。
总的来说，稳定排序算法对于某些应用非常重要，例如需要按照多个关键字进行排序的场合。在这种情况下，如果使用不稳定排序算法进行排序，可能会导致结果不正确。因此，在选择排序算法时，需要根据具体应用场景和要求来选择不同的排序算法。

'''
import random
from typing import List



import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums
    def quick_sort(self, nums, start, end):
        if start>=end:
            return

        pivot = random.randint(start, end)
        nums[end], nums[pivot] = nums[pivot], nums[end]
        pivot_num = nums[end]
        i, j = start, end-1
        while i<=j:
            while i<=j and nums[i]<pivot_num:
                i+=1
            while i<=j and nums[j]>pivot_num:
                j-=1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        nums[i], nums[end] = nums[end], nums[i]
        self.quick_sort(nums, start, i-1)
        self.quick_sort(nums, i+1, end)
    
class Solution: # 这个好记，但是会使用额外的存储
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            pivot = random.choice(nums)
            left = []
            right = []
            mid = []
            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num == pivot:
                    mid.append(num)
                else:
                    right.append(num)
            return self.sortArray(left) + mid + self.sortArray(right)





s = Solution()
res = s.sortArray([5,2,3,1])
print(res)