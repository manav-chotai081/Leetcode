class Solution:
    def minimumSum(self, num: int) -> int:
        digit = []
        while num > 0:
            digit.append(num%10)
            num = num // 10
        digit.sort()
        d1 = digit[0] * 10 + digit[3]
        d2 = digit[1] * 10 + digit[2]
        return d1 + d2
        