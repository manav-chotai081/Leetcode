class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            temp = str(i)
            if len(temp) % 2 == 0:
                ans += 1
        return ans
        