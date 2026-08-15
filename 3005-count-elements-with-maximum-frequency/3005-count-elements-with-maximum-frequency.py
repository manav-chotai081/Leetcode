class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num = list(set(nums))
        count = []
        for i in num:
            count.append(nums.count(i))
        ans = max(count)
        ans *= count.count(ans)
        return ans

        