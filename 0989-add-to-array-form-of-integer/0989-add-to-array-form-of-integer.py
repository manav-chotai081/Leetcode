class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = 0
        for i in range(len(num)):
            ans *= 10
            ans += num[i]
        ans += k
        ans1 = []
        while ans>0:
            ans1.append(ans % 10)
            ans = ans // 10
        ans1 = ans1[::-1]
        return ans1

        