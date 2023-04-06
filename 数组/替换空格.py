"https://leetcode.cn/problems/ti-huan-kong-ge-lcof/description/"

class Solution:
    def replaceSpace(self, s: str) -> str:

        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res
