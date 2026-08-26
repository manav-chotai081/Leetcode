class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = {}
        for i in s:
            if i not in s1:
                s1[i] = 1
        for i in s1.keys():
            if s.count(i) == 1:
                return s.index(i)
        return -1

        