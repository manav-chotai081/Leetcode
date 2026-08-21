class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num = list(set(nums))
        for i in num:
            nums.remove(i)
        return nums[0]
        