class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        square = []
        for i in nums:
            square.append(i*i)
        square.sort()
        n = len(square) // 2
        ans = 0
        for i in range(n):
            ans -= square[i]
        for i in range(n, len(square)):
            ans += square[i]
        return ans



        