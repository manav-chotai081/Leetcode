class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(len(nums)):
            if n % (i+1) == 0:
                ans += nums[i] * nums[i]
        return ans

        