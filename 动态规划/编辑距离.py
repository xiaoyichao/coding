class Solution: #普通的递归，果然超时啦
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        return self.dp(word1,m-1, word2,n-1)

    def dp(self,word1,i, word2,j):
        # base case
        if (i==-1) :
            return j+1
        if (j==-1):
            return i+1
        # 无需改变的位置
        if word1[i] == word2[j]:
            return self.dp(word1,i-1, word2,j-1)
        # 需改变的位置
        return min(
            self.dp(word1,i, word2,j-1) +1, #插入
            self.dp(word1,i-1, word2,j) +1, #删除
            self.dp(word1,i-1, word2,j-1) +1, #替换
        )


class Solution: #备忘录+递归
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        mem = [[-1]*n for _ in range(m)]
        return self.dp(word1,m-1, word2,n-1,mem)

    def dp(self,word1,i, word2,j, mem):
        # base case
        if (i==-1) :
            return j+1
        if (j==-1):
            return i+1
        # 无需改变的位置
        if word1[i] == word2[j]:
            return self.dp(word1,i-1, word2,j-1,mem)
        if mem[i][j] != -1:
            return mem[i][j]
        # 需改变的位置
        res = min(
            self.dp(word1,i, word2,j-1, mem) +1, #插入
            self.dp(word1,i-1, word2,j, mem) +1, #删除
            self.dp(word1,i-1, word2,j-1, mem) +1, #替换
        )
        mem[i][j] = res 
        return mem[i][j]


class Solution: # DP + 迭代
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                    # dp[i-1][j] 表示将 word1 的前 i-1 个字符转换成 word2 的前 j 个字符所需的最少操作数，然后再在 word1 的第 i 个位置插入一个字符。
                    # dp[i][j-1] 表示将 word1 的前 i 个字符转换成 word2 的前 j-1 个字符所需的最少操作数，然后再在 word2 的第 j 个位置插入一个字符。
                    # dp[i-1][j-1] 表示将 word1 的前 i-1 个字符转换成 word2 的前 j-1 个字符所需的最少操作数，然后再将 word1 的第 i 个位置替换成 word2 的第 j 个位置的字符。
        
        return dp[m][n]

      
    
s = Solution()
res = s.minDistance("abc", "ab")
print(res)

