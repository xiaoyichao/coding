# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao
Date: 2022-07-28 22:02:26
LastEditTime: 2023-01-30 14:45:58
Description: https://leetcode.cn/problems/minimum-window-substring/

'''
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        # 记录分别每个字母需要几次
        for i in t:
            need[i] = need[i]+1

        window = defaultdict(int)  
        l = 0
        r = 0 
        valid = 0 #用来记录need中需要的，是否windows中都满足了
        start = -1
        min_len = float('inf')
        # 右指针一直往后移动，直到满足需求，说明找到了一个解
        while r < len(s) :
            # 窗口字典的数据更新
            c = s[r]
            r+=1
            if c in need:
                window[c] += 1
                if window[c] == need[c]: # 判断某个字母所需要的数字是否在窗口中是否已经满足
                    valid+=1
            # 左指针往右移动，看是否能优化这个解答
            while (valid == len(need)): # need中需要的，windows中都满足了
                # print("满足数据", s[l:r+1]) # 字符串是左闭右开，所以需要右边+1才能取到
                # 更新最小子串的记录，也就是找到了更短的子串
                if (r-l)<min_len:
                    start = l
                    min_len = r-l
                    # print("更新数据",s[start:start+min_len])
                # 更新窗口字典
                d = s[l]
                l+=1
                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -= 1 # 这个位置注意window[d] -= 1的操作 会影响if window[d] == need[d]的判断结果，所以得注意写在IF的后边
     
        return "" if min_len == float('inf') else s[start:start+min_len]


# 下边这个是for循环写的，尽量别看
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for i in t:
            need[i] = need[i]+1
        window = defaultdict(int)  
        l = 0
        # r = -1 
        valid = 0 #用来记录need中需要的，是否windows中都满足了
        start = -1
        min_len = float('inf')
        # while r < len(s)-1 :
        for r in range(len(s)): # 注释的地方是两种不同的写法
            # r+=1
            # 窗口字典的数据更新
            c = s[r]
            if c in need:
                window[c] += 1
                if window[c] == need[c]: # 判断某个字母所需要的数字是否在窗口中是否已经满足
                    valid+=1
            
            while (valid == len(need)): # need中需要的，windows中都满足了
                # print("满足数据", s[l:r+1]) # 字符串是左闭右开，所以需要右边+1才能取到
                # 更新最小子串的记录，也就是找到了更短的子串
                if (r-l+1)<min_len:
                    start = l
                    min_len = r-l+1
                    # print("更新数据",s[start:start+min_len])
                # 更新窗口字典
                d = s[l]
                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -= 1 # 这个位置注意window[d] -= 1的操作 会影响if window[d] == need[d]的判断结果，所以得注意写在IF的后边

                    
                l+=1
                
        return "" if min_len == float('inf') else s[start:start+min_len]


s= Solution()
res = s.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(res)
            
