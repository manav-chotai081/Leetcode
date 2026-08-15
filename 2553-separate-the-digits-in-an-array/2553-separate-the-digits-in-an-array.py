class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            temp = str(i)
            for j in temp:
                ans.append(int(j))
        return ans