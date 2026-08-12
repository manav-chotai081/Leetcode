class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ''
        for i in order:
            if i in s:
                temp = s.count(i)
                for j in range(temp):
                    ans+=i
        for i in s:
            if i not in ans:
                temp = s.count(i)
                for j in range(temp):
                    ans+=i
        return ans
        