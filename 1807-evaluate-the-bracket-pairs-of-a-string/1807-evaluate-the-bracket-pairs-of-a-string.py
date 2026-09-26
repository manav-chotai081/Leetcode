class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = {}
        for i in knowledge:
            ans[i[0]] = i[1]
        t = ''
        ans1 = ''
        for i in s:
            if i == '(':
                ans1 += t
                t = ''

            elif i == ')':
                if t in ans:
                    ans1 += ans[t]
                else:
                    ans1 += '?'
                t = ''
            else:
                t += i
        ans1 += t
        return ans1
