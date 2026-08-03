class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        ans = ''
        for i in range(len(word)-1,-1,-1):
            ans += word[i]
            ans += " "
        return ans.strip()
        
            
        