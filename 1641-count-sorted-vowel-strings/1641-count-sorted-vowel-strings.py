class Solution:
    def countVowelStrings(self, n: int) -> int:
        r = 5
        ans = 1
        for i in range(1,n+1):
            ans = ans* (r+i-1)//i
        return ans
        