# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-30 10:28:10
LastEditTime: 2023-01-30 14:18:04
Description: https://leetcode.cn/problems/permutation-in-string/
'''
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        valid = 0
        need = defaultdict(int)
        window = defaultdict(int)
        for x in s1:
            need[x] += 1

        for r in range(len(s2)):
            # 窗口数据更新
            c = s2[r]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while (r-l+1 >= len(s1)):  # 判断l 指针右移的条件

                if valid == len(need):
                    return True

                d = s2[l]
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1  # 这个位置注意window[d] -= 1的操作 会影响if window[d] == need[d]的判断结果，所以得注意写在IF的后边
                l += 1
        return False

s=Solution()
# res = s.checkInclusion(s1 = "ab", s2 = "eidbaooo")
res = s.checkInclusion(s1= "ab", s2 = "eidboaoo")

print(res)
