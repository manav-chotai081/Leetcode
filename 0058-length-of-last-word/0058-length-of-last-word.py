class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()
        
        return len(ans[len(ans)-1])
        