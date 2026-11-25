class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        start = 0
        arr = []
        for i in spaces:
            arr.append(s[start:i])
            start = i
        arr.append(s[start:])
        s1 = ''
        for i in arr:
            s1 += i
            s1 += " "
        s1 = s1.strip()
        if 0 in spaces:
            s1 = ' ' + s1
        if len(s) in spaces:
            s1 = s1 + ' '
        return s1
            
        