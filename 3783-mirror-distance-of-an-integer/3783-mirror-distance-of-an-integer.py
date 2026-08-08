class Solution:
    def mirrorDistance(self, n: int) -> int:
        # s = str(n)
        # s = s[::-1]
        # n1 = int(s)
        # return abs(n-n1)

        s = str(n)
        return abs(n-int(s[::-1]))