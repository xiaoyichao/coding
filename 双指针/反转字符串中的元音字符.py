# coding=UTF-8
'''
Author: xiaoyichao
LastEditors: Please set LastEditors
Date: 2021-03-30 21:53:32
LastEditTime: 2022-05-11 11:31:20
Description: https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
'''
from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        s =  list(s)
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i < j:
            if s[i] in vowel_set and s[j] in vowel_set:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vowel_set:
                i += 1
            elif s[j] not in vowel_set:
                j -= 1
        return "".join(s)
