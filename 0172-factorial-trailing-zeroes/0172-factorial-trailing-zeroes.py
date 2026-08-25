class Solution:
    def trailingZeroes(self, n: int) -> int:
        c2 = 0
        c5 = 0
        for i in range(1,n+1):
            temp = i
            while True:
                if temp % 2 == 0:
                    c2 += 1
                    temp = temp // 2
                else:
                    break
            temp = i
            while True:
                if temp % 5 == 0:
                    c5 += 1
                    temp = temp // 5
                else:
                    break 
        return min(c2,c5)
        