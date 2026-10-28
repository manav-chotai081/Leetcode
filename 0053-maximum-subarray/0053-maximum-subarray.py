class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = float('-inf') 
        current = float('-inf') 
        for i in nums:
            current = max(i, current+i)
            maximum = max(current, maximum)
        return maximum
        