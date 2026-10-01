class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = []
        for i in s:
            ans.append(i)
        return len(list(set(ans)))        