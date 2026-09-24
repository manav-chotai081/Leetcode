class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        temp = 0
        dummy = 0
        if len(nums) > 0 and nums[0] == 0:
            return 0
        for i in range(len(nums)):
            dummy = nums[i]
            temp = 0
            while dummy > 0:
                temp += dummy % 10
                dummy = dummy // 10
            if temp == i:
                return i
        return -1

        