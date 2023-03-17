# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: xiaoyichao xiao_yi_chao@163.com
Date: 2022-12-13 15:38:18
LastEditTime: 2023-02-03 09:28:46
Description: https://leetcode.cn/problems/longest-substring-without-repeating-characters/

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 用于存储不重复字符的集合
        n = len(s)
        right = 0  # 滑动窗口的右指针
        max_len = 0  # 用于记录最长子串长度

        for left in range(n):
            while right < n and s[right] not in char_set:
                char_set.add(s[right])
                right += 1

            max_len = max(max_len, len(char_set))  # 更新最长子串长度
            char_set.remove(s[left])  # 移除左指针对应的字符，滑动窗口左边界向右移动

        return max_len
    
# 我的解法
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        win_set = set()

        left,right= 0,0
        
        while right<len(s):
            if s[right] not in win_set:
                win_set.add(s[right])
                res = max(res, len(win_set))
                right +=1
            else:
                win_set.remove(s[left])
                left+=1       
        return res
    

# labuladong 的解法
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l = 0 
        r = 0
        count = 0

        while r<len(s):
            c = s[r]
            r+=1
            window[c] +=1
                
            while window[c] >1 :
                d = s[l]
                l+=1
                window[d] -=1
            count = max(count,r-l)  # 这个位置不能写count = max(count,len(window)) 因为进入过window的数据，即使value =0 但是key也存在
        return count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk+1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, len(occ))  # len(occ) 是现在的结果。
            # ans = max(ans, rk - i + 1)  # （rk - i + 1）是现在的结果。ans在max计算之前是从前的结果。
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:

        occ = set()
        n = len(s)
        ans = 0
        rk = -1
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in occ:
            # while s[rk+1] not in occ and rk+1 < n:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, len(occ))
            # ans = max(ans, rk - i + 1)
        return ans

s = Solution()
ans = s.lengthOfLongestSubstring("abcabcbb")
print(ans)
