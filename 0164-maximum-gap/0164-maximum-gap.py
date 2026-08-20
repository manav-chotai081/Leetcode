class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 2:
            return 0
        ans = 0
        temp = 0
        for i in range(1,len(nums)):
            temp = nums[i] - nums[i-1]
            if temp > ans:
                ans = temp
        return ans

        