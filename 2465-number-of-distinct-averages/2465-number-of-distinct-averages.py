class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)//2):
            max1 = max(nums)
            min1 = min(nums)
            ans.append((max1+min1)/2)
            nums.remove(max1)
            nums.remove(min1)
        ans1 = list(set(ans))
        return len(ans1)
        