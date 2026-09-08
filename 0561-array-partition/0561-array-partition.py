class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num = sorted(nums)
        ans = 0
        for i in range(0,len(nums),2):
            ans += min(num[i], num[i+1])
        return ans

        