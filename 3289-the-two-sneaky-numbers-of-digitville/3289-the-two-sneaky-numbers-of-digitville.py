class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = {}
        value = []
        for i in nums:
            if i not in ans:
                ans[i] = 1
            else:
                value.append(i)
        return value
        