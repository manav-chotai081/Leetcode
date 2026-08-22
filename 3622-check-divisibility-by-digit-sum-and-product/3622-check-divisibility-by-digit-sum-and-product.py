class Solution:
    def checkDivisibility(self, num: int) -> bool:
        sum1 = 0
        product = 1
        n = num
        while n > 0:
            temp = n % 10
            sum1 += temp
            product *= temp
            n = n // 10
        ans = (sum1 + product)
        if num % ans == 0:
            return True
        else:
            return False
        