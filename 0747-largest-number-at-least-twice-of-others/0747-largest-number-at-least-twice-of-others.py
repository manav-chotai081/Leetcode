class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max(nums)
        for i in nums:
            if i*2 > max1 and i != max1:
                return -1
        return nums.index(max1)
        