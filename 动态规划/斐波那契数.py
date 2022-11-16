class Solution:
    def fib(self, n: int) -> int: # 递归
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    def fib_2(self, n:int)-> int: #动态规划（必然使用缓存）
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
    def fib_3(self, n:int)-> int: #动态规划 + 只记住两个数的缓存
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

        
s = Solution()
res = s.fib_3(3)
print(res)