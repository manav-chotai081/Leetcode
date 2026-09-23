class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        ans = []
        count = 0
        flag = ''
        for k in words:
            i = k.lower()
            count = 0
            if i[0] in r1:
                flag = r1
            elif i[0] in r2:
                flag = r2
            else:
                flag = r3
            for j in i:
                if j in flag:
                    count += 1
                else:
                    break
            if count == len(i):
                ans.append(k)
        return ans

        