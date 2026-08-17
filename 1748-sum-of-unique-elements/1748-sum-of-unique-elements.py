class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num = list(set(nums))
        ans = 0
        for i in num:
            if nums.count(i) == 1:
                ans += i
        return ans
        