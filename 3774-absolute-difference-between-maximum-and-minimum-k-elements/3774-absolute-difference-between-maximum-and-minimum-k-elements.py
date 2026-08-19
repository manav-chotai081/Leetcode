class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        num = nums[::]
        max1 = 0
        min1 = 0
        for i in range(k):
            max1 += max(nums)
            nums.remove(max(nums))
            min1 += min(num)
            num.remove(min(num))
        return abs(max1-min1)

        