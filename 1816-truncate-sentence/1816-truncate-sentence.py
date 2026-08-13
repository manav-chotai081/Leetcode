class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = s.split()
        ans1 = ''
        for i in range(k):
            ans1+=ans[i]
            ans1 += " "
        return ans1.strip()

        