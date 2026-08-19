class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        num = list(set(nums))
        num.sort(reverse = True)
        ans = []
        if k > len(num):
            k = len(num)
        for i in range(k):
            ans.append(num[i])
        return ans
        