class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                v += 1
            elif i.isalpha():
                c+=1
        if c > 0:
            return v // c
        return 0

        