class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = nums[::]
        num.sort()
        ans = []
        for i in nums:
            temp = num.index(i)
            ans.append(temp)

        return ans       