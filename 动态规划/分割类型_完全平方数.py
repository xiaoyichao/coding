'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)    
        for i in range(1, n+1):
            dp[i] = i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        return dp[-1]
s = Solution()
res = s.numSquares(10)
print(res)