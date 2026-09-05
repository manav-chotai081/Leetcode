class Solution:
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
        for i in range(k):
            min1 = min(nums)
            ind = nums.index(min1)
            nums[ind] *= mul
        return nums
        