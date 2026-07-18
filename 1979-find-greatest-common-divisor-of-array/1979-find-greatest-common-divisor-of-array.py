class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        gcd = 1
        for i in range(2,minimum+1):
            if minimum % i == 0 and maximum % i == 0:
                gcd = i
        return gcd
        