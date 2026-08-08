class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums[::]
        for i in range(len(nums)-1, -1,-1):
            ans.append(nums[i])
        return ans

        