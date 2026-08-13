class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        len1= len(ans)
        return len(ans[len1-1])
        