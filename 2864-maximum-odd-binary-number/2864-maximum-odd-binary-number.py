class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1 = s.count('1')
        c2 = s.count('0')
        c1 -= 1
        s1 = '1'*c1
        s1 += '0'*c2
        s1 += '1'
        return s1

        