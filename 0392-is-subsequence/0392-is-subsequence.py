class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len1 = len(t)
        len2 = len(s)
        for i in range(len2):
            if s[i] in t:
                temp = t.index(s[i])
                t1 = ''
                for i in range(temp+1,len(t)):
                    t1 += t[i]
                t = t1
            else:
                return False
        return True
                