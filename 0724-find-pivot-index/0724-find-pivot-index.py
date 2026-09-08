class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # if len(num) == 2:
        #     if nums[1] == 0:
        #         return 0
        #     else:
        #         return -1
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        return -1
        
        