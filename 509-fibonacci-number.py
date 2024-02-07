class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        f1 = self.fib(n-1)
        f2 = self.fib(n-2)
        return f1+f2
