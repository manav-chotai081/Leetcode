class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)):
            temp = t.index(s[i])
            ans += abs(i-temp)
        return ans