class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if index[i] == i:
                ans.append(nums[i])
            else:
                ans.insert(index[i], nums[i])
        return ans

        