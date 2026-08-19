class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max1 = max(nums)
        ans = k*max1
        ans += (k*(k-1))//2
        return ans
        