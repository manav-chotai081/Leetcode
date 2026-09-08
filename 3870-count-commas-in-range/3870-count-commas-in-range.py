class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        ans = 0
        n = n - 999
        return n
        