class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = 1
        while True:
            if n < temp:
                return False
            if n == temp:
                return True
            temp *= 3
             

        