class Solution:
    def shortestPalindrome(self, s: str) -> str:
        temp = ''
        for i in range(len(s)):
            temp = s[:len(s)-i]
            if temp == temp[::-1]:
                break
        ans1 = s
        new = ans1.replace(temp,"",1)
        new = new[::-1]
        new = new + s
        return new
        

            
        