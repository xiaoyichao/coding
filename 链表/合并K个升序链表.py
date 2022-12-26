# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2022-12-23 09:21:58
LastEditTime: 2022-12-23 09:26:45
Description: 

作者：qsinsong
链接：https://leetcode.cn/problems/merge-k-sorted-lists/solution/python-23he-bing-kge-sheng-xu-lian-biao-ep54a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

import heapq
from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        # 将堆进行初始化
        stack = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                stack.append([lists[i].val, i])
        heapq.heapify(stack)
        
        # 依次出队有序合并
        ans = ListNode(-1)
        cur = ans
        while stack:
            _, i = heapq.heappop(stack)
            temp = lists[i].next
            lists[i].next = None
            cur.next = lists[i]
            cur = cur.next
            if temp:
                lists[i] = temp
                heapq.heappush(stack, [lists[i].val, i])
        return ans.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq #调用堆
        minHeap = []
        for listi in lists: 
            while listi:
                heapq.heappush(minHeap, listi.val) #把listi中的数据逐个加到堆中
                listi = listi.next
        dummy = ListNode(0) #构造虚节点
        p = dummy
        while minHeap:
            p.next = ListNode(heapq.heappop(minHeap)) #依次弹出最小堆的数据
            p = p.next
        return dummy.next 

