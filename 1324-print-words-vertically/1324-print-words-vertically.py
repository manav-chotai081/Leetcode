class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        maximum = 0
        times = 0
        for i in arr:
            if len(i) > maximum:
                maximum = len(i)
                
        ans = [''] *maximum
        for i in arr:
            for j in range(len(i)):
                ans[j] += i[j]
            for j in range(len(i),maximum):
                ans[j] += ' '
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()
        return ans

        