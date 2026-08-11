class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = []
        if len(s) != len(t):
            return False
        for i in range(len(t)):
            c1.append(t[i])
        c2 = []
        for i in range(len(s)):
            c2.append(s[i])
        for i in c1:
            if i in c2:
                c2.remove(i)
            else:
                return False
        return True
        



        