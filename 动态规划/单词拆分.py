"https://leetcode.cn/problems/word-break/"

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 创建一个set，将wordDict转为set，方便查找
        word_set = set(wordDict)
        # 创建一个布尔数组，表示到当前位置的子串能否被分割成字典中的单词
        dp = [False] * (len(s) + 1)
        # 初始状态，空串可以被分割成字典中的单词
        dp[0] = True

        # 遍历s的每个字符
        for i in range(len(s)):
            # 遍历从0到i的子串
            for j in range(i+1):
                # 如果dp[j]为True，表示0到j-1的子串可以被分割成字典中的单词
                # 并且[j:i+1]这个子串在字典中出现过
                if dp[j] and s[j:i+1] in word_set:
                    # 更新dp数组
                    dp[i+1] = True
                    break
        # 返回dp数组的最后一个值，表示整个s是否可以被分割成字典中的单词
        return dp[-1]
    

s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))

    

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