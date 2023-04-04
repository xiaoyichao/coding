'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

链接：https://leetcode.cn/problems/perfect-squares


'''
import math

class Solution: #递归
    def numSquares(self, n: int) -> int:
        min_num = n
        i = 1
        while i*i <= n:
            min_num = min(min_num, self.numSquares(n - i*i) + 1)
            i += 1
        return min_num

class Solution: #带备忘录的递归
    def numSquares(self, n: int, mem = {}) -> int:
        if n in mem:
            return mem[n]
        min_num = n
        i = 1
        while i*i <= n:
            min_num = min(min_num, self.numSquares(n - i*i, mem) + 1)
            mem[n] = min_num
            i += 1
        return min_num


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)    
        for i in range(1, n+1):
            dp[i] = i  # 最坏的结果就是全是1的平方构成，i等于几，就是几个完全平方数构成
            max_range = int(math.sqrt(i))
            for j in range(1,max_range+1):
                max_dp = dp[i]
                tmp_dp = dp[i-j*j]
                dp[i] = min(max_dp, tmp_dp + 1)  # 穷举 1 到 int(math.sqrt(i)) 的情况 ，有点递归的意思，通过记忆化等方法弄掉重复计算
        return dp[-1]
s = Solution()
res = s.numSquares(12)
print(res)