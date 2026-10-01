class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = []
        for i in s:
            ans.append(i)
        ans1 = list(dict.fromkeys(ans))
        return len(ans1)        