# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao
Date: 2023-01-30 10:28:10
LastEditTime: 2023-01-30 14:49:01
Description: https://leetcode.cn/problems/permutation-in-string/
'''
from collections import defaultdict


from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0  # 窗口左边界指针
        r = 0  # 窗口右边界指针
        valid = 0  # 记录窗口中满足要求的字符数
        need = defaultdict(int)  # 记录s1中每个字符出现的次数
        window = defaultdict(int)  # 记录窗口中每个字符出现的次数
        for x in s1:
            need[x] += 1  # 统计s1中每个字符出现的次数

        while r < len(s2):
            # 窗口数据更新
            c = s2[r]  # 窗口右边界向右移动一位，获取新加入的字符
            r += 1
            if c in need:
                window[c] += 1  # 更新窗口中新加入的字符出现的次数
                if window[c] == need[c]:
                    valid += 1  # 如果新加入的字符出现的次数满足要求，则valid加1
            while (r-l >= len(s1)):  # 判断窗口大小是否满足要求

                if valid == len(need):  # 如果窗口中满足要求的字符数等于s1中的字符数，说明找到了s1的排列
                    return True

                d = s2[l]  # 窗口左边界向右移动一位，获取移出的字符
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1  # 如果移出的字符出现的次数满足要求，则valid减1
                    window[d] -= 1  # 更新窗口中移出的字符出现的次数

        return False  # 如果没有找到s1的排列，则返回False

        

# 下边这个是for循环写的，尽量别看       
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
