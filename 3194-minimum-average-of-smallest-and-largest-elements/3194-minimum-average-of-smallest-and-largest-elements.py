class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = []
        for i in range(len(nums)//2):
            min1 = min(nums)
            max1 = max(nums)
            nums.remove(min1)
            nums.remove(max1)
            ans.append((min1+max1)/2)
        return min(ans)

        