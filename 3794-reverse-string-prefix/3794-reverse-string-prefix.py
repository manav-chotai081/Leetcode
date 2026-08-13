class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ans = ''
        for i in range(k-1, -1, -1):
            ans += s[i]
        for i in range(k, len(s)):
            ans += s[i]
        return ans
        