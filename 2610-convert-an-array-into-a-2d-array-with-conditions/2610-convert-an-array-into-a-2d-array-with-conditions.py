class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ans = {}
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        max1 = max(list(ans.values()))
        final = []
        for i in range(max1):
            row = []
            for i, j in ans.items():
                if j > 0:
                    row.append(i)
                    ans[i] -= 1
            final.append(row)
        return final
            

        