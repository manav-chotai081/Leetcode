class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ans1 = abs(z-x)
        ans2 = abs(z-y)
        if ans1 > ans2:
            return 2
        if ans1 < ans2:
            return 1
        return 0
        