class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        x1 = str(x)
        x2 = x1[::-1]
        if x1 == x2:
            return True
        return False

        