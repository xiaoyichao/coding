"https://leetcode.cn/problems/fibonacci-number/"

class Solution:
    def fib(self, n: int) -> int: # 递归
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    
class Solution: #带备忘录的递归
    def fib(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]
class Solution:
    def fib(self, n:int)-> int: #动态规划 DP table
        res = []
        for i in range(0,n+1,1):
            if i==0:
                res.append(0)
            elif i==1:
                res.append(1)
            else:
                tmp = res[-1] + res[-2]
                res.append(tmp)
        return res[-1]
class Solution:
    def fib(self, n:int)-> int: #动态规划 + 只记住两个数的 DP table
        a = 0
        b = 0
        for i in range(0,n+1,1):
            if i==0:
                a=0
                a,b = b, a+b
            elif i==1:
                a=1
                a,b = b, a+b
            else:
                a,b = b, a+b
        return b

class Solution:
    def fib(self, n: int) -> int:
        for i in range(0,n+1,1):
            if i ==0:
                a = 0
                b=0
            elif i ==1:
                b=1
            else:
                a,b = b, a+b
        return b
    

s = Solution()
res = s.fib(10)
print(res)