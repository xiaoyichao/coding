"https://leetcode.cn/problems/word-break/"

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 创建一个布尔数组 dp，其中 dp[i] 表示字符串 s 的前 i 个字符是否可以被 wordDict 中的单词拼接出
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        # 遍历整个字符串 s
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        # 返回 dp[n]，表示整个字符串 s 是否可以被 wordDict 中的单词拼接出
        return dp[n]

    

class Solution:
    def __init__(self):
        # 备忘录
        self.memo = []
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 备忘录，-1 代表未计算，0 代表 false，1 代表 true
        self.memo = [-1] * len(s)
        
        # 根据函数定义，判断 s[0..] 是否能够被拼出
        return self.dp(s, 0, wordDict)
    
    # 定义：返回 s[i..] 是否能够被 wordDict 拼出
    def dp(self, s: str, i: int, wordDict: List[str]) -> bool:
        # base case，整个 s 都被拼出来了
        if i == len(s):
            return True
        
        # 防止冗余计算
        if self.memo[i] != -1:
            return True if self.memo[i] == 1 else False
        
        # 遍历所有单词，尝试匹配 s[i..] 的前缀
        for word in wordDict:
            length = len(word)
            if i + length > len(s):
                continue
            sub_str = s[i:i+length]
            
            if sub_str != word:
                continue
                
            # s[i..] 的前缀被匹配，去尝试匹配 s[i+len..]
            if self.dp(s, i+length, wordDict):
                # s[i..] 可以被拼出，将结果记入备忘录
                self.memo[i] = 1
                return True
        
        # s[i..] 不能被拼出，结果记入备忘录
        self.memo[i] = 0
        return False