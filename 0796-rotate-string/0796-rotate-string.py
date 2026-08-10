class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # s1 = goal[0]
        # i1 = s.find(s1)
        # len1 = len(s)
        # for i in range(i1,len1):
        #     if s[i] != goal[i-i1]:
        #         return False  
        # return True
        for i in range(len(s)):
            s = s[len(s)-1] + s
            s = s[:-1]
            if s == goal:
                return True
        return False