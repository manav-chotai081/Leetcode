class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nums = str(n)
        ans = 0
        for i in range(0,len(nums)):
            if i % 2 == 0:
                ans += int(nums[i])
            else :
                ans -= int(nums[i])
        return ans

        