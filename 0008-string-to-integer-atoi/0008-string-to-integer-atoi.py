class Solution:
    def myAtoi(self, s: str) -> int:
        s1 = s.strip()
        ans = 0
        if len(s1) == 0:
            return 0
        if s1[0]=='-':
            s2 = '0'
            length = len(s1)
            for i in range(1,length):
                if s1[i].isdigit():
                    s2 += s1[i]
                else:
                    break
            ans = int(s2)
            if ans > 2147483648:
                return -2147483648
            ans *= (-1)
            return ans
        elif s1[0] == '+':
            s2 = '0'
            length = len(s1)
            for i in range(1,length):
                if s1[i].isdigit():
                    s2 += s1[i]
                else:
                    break
            ans = int(s2)
            if ans > 2147483647:
                return 2147483647
            return ans
        else  : 
            s2 = '0'
            length = len(s1)
            for i in range(0,length):
                if s1[i].isdigit():
                    s2 += s1[i]
                else:
                    break
            ans = int(s2)
            if ans > 2147483647:
                return 2147483647
            return ans
        return 0

        