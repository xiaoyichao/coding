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
        # 定义 dp 数组，其中 dp[i] 表示数字 i 最少可以由多少个完全平方数组成
        dp = [0] * (n+1)

        for i in range(1, n+1):
            # 先将 dp[i] 设为 i，即全部用 1^2 组成
            dp[i] = i

            # 遍历所有小于 i 的完全平方数 j^2，将 dp[i-j^2] 的值加上 1 的结果与 dp[i] 进行比较，取较小值即可
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)

        return dp[n]

s = Solution()
res = s.numSquares(4)
print(res)