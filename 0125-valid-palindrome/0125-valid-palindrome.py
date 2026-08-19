class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                ans += i
        if ans == ans[::-1]:
            return True
        return False
        