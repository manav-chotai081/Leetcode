class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split()
        ans1 = [0]*len(ans)
        for i in ans:
            temp = i[len(i)-1]
            ans1[int(temp)-1] = i.replace(temp, '')
        s1 = ''
        for i in ans1:
            s1 += i + ' '
        return s1.strip()        