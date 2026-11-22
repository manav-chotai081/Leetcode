class Solution:
    def checkString(self, s: str) -> bool:
        a = s.count('a')
        for i in s:
            if i == 'a':
                a -= 1
            elif a == 0:
                return True
            else:
                return False
        return True

        