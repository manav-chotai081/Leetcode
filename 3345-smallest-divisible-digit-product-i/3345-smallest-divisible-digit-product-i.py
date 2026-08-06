class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(10):
            mul = 1
            copy = n + i
            while copy > 0:
                rem = copy % 10
                mul *= rem
                copy = copy // 10
            if mul % t == 0:
                return n + i
        
        