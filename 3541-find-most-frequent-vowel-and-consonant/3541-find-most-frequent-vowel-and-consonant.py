class Solution:
    def maxFreqSum(self, s: str) -> int:
        s1 = []
        for i in s:
            s1.append(i)
        s2 = list(set(s1))
        v1 = 0
        c1 = 0
        for i in s2:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                temp = s1.count(i)
                if v1 < temp:
                    v1 = temp
            else:
                temp = s1.count(i)
                if c1 < temp:
                    c1 = temp
        return v1 + c1
        