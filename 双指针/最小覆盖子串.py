# coding=UTF-8
'''
Author: 
LastEditors: xiaoyichao xiao_yi_chao@163.com
Date: 2022-07-28 22:02:26
LastEditTime: 2023-01-30 00:24:23
Description: https://leetcode.cn/problems/minimum-window-substring/

'''
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = defaultdict(int)
        for i in t:
            need_dict[i] = need_dict[i]+1
        windows_dict = defaultdict(int)  
        l = 0
        # r = -1 
        valid = 0 #用来记录need中需要的，是否windows中都满足了
        start = -1
        min_len = float('inf')
        # while r < len(s)-1 :
        for r in range(len(s)): # 注释的地方是两种不同的写法
            # r+=1
            # 窗口字典的数据更新
            if s[r] in need_dict:
                windows_dict[s[r]] += 1
                if windows_dict[s[r]] == need_dict[s[r]]: # 判断某个字母所需要的数字是否在窗口中是否已经满足
                    valid+=1
            
            while (valid == len(need_dict)): # need中需要的，windows中都满足了
                # print("满足数据", s[l:r+1]) # 字符串是左闭右开，所以需要右边+1才能取到
                # 更新最小子串的记录，也就是找到了更短的子串
                if (r-l+1)<min_len:
                    start = l
                    min_len = r-l+1
                    # print("更新数据",s[start:start+min_len])
                # 更新窗口字典
                
                if s[l] in need_dict:
                    windows_dict[s[l]] -= 1
                    if windows_dict[s[l]] < need_dict[s[l]]:
                        valid -=1
                l+=1
                
        return "" if min_len == float('inf') else s[start:start+min_len]

s= Solution()
res = s.minWindow(s = "ADOBECODEBANC", t = "ABC")
print(res)
            
