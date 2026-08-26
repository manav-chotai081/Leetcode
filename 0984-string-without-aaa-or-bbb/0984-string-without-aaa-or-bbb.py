class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        temp = ''
        if a == 0:
            for i in range(b):
                temp += 'a'
            return temp
        if b == 0:
            for i in range(a):
                temp += 'b'
            return temp
        if a > b:
            while a > b:
                ans = min(2,a)
                for i in range(ans):
                    temp += 'a'
                    a -= 1
                if b > 0:
                    temp += 'b'
                    b -= 1
            while a > 0:
                temp += 'ab'
                a -= 1
                b -= 1
            return temp
        if a < b:
            while a < b:
                ans = min(2,b)
                for i in range(ans):
                    temp += 'b'
                    b -= 1
                if a > 0:
                    temp += 'a'
                    a -= 1
            while a > 0:
                temp += 'ab'
                a -= 1
                b -= 1
            return temp
        for i in range(a):
            temp += 'ab'
        return temp
        