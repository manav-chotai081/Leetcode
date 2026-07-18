class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        element = []
        nums.sort()
        if length == 1:
            return element
        for i in range(0,length-1):
            if nums[i] == nums[i+1]:
                element.append(nums[i])
        return element



        