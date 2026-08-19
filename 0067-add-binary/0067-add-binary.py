class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a  =a[::-1]
        b = b[::-1]
        temp = 1
        a1 = 0
        for i in a:
            a1 += temp*int(i)
            temp *= 2
        temp = 1
        b1 = 0
        for j in b:
            b1 += temp*int(j)
            temp *= 2
        ans = a1 + b1
        ans1 = ''
        if ans == 0:
            return '0'
        while ans > 0:
            ans1 = str(ans % 2) + ans1
            ans = ans // 2
        return ans1


        