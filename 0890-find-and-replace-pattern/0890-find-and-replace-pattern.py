class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        p = {}
        for i in pattern:
            if i not in p:
                p[i] = 1
            else:
                p[i] += 1
        temp = {}
        ans = []
        count = 0
        for i in words:
            temp = {}
            p = {}
            count = 0
            for j, k in zip(i, pattern):
                if (j not in temp) and (k not in p):
                    temp[j] = 1
                    p[k] = 1
                    count += 1
                elif (j in temp) and (k in p):
                    temp[j] += 1
                    p[k] += 1
                    count += 1
                else:
                    break
            if count == len(i) and list(p.values()) == list(temp.values()):
                ans.append(i)
        return ans
        