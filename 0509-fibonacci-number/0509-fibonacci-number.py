class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1 = 1
        f0 = 0
        f2 = 0
        for i in range(2,n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2

        