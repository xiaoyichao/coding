'''
这个题目是一维动态规划的题目

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
https://leetcode.cn/problems/climbing-stairs/
  

这是十分经典的斐波那契数列题。定义一个数组 dp，dp[i] 表示走到第 i 阶的方法数。
因为 我们每次可以走一步或者两步，所以第 i 阶可以从第 i-1 或 i-2 阶到达。
换句话说，走到第 i 阶的 方法数即为走到第 i-1 阶的方法数加上走到第 i-2 阶的方法数。
这样我们就得到了状态转移方程 dp[i] = dp[i-1] + dp[i-2]。注意边界条件的处理。

这个文章不错
https://leetcode.cn/problems/climbing-stairs/solution/zhi-xin-hua-shi-pa-lou-ti-zhi-cong-bao-l-lo1t/
'''

class Solution:
    def climbStairs(self, n: int) -> int: #  动态规划+缓存
        dp = [0]*(n+1) # 构造缓存list , 第0个台阶的情况要考虑，所以是n+1个
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2] # 记录结果，从第 i-1 阶的方法数迈一步 或者 走到第 i-2 阶的方法数迈两步 即可到第 i 阶， 所以走到第 i 阶的 方法数是这两个情况的加和。
        return dp[-1]

    # f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
    def climbStairs_1(self, n: int) -> int: # 动态规划+两位缓存
        a = 1
        b = 1
        for i in range(2, n+1):
            # tmp = a
            # a = b
            # b = tmp+b
            a, b = b, a + b
        return b


if __name__ == '__main__':
    S = Solution()
    print(S.climbStairs(3))
