class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        num = list(dict.fromkeys(nums))
        for i in num:
            if nums.count(i) == 1 and i % 2 == 0:
                return i
        return -1
        