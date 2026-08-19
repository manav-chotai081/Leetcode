class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = sum(nums)
        digits = 0
        for i in range(len(nums)):
            temp = nums[i]
            while temp > 0:
                digits += temp%10
                temp = temp // 10
        return abs(digits - ans)
        