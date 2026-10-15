class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                ans += len(list(set(nums[j:j+i+1]))) ** 2
        return ans


        