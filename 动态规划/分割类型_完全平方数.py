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