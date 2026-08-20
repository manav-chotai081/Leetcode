class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = list(set(nums))
        nums.sort()
        num.sort()
        j = 0
        for i in range(len(num)):
            if nums[i] != num[j]:
                return nums[i]
            j += 1
        return nums[len(nums) - 1]
