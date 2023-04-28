
"https://leetcode.cn/problems/power-of-two/"
# 一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1。

# 位运算 n&(n-1) 在算法中挺常见的，作用是消除数字 n 的二进制表示中的最后一个 1，用这个技巧可以判断 2 的指数。

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

