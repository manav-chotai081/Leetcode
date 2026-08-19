class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for i in details:
            temp = i[11]
            temp += i[12]
            temp = int(temp)
            if temp > 60:
                ans += 1
        return ans

        