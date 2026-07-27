class Solution:
    def thirdMax(self, num: List[int]) -> int:
        count = 1
        nums = list(set(num))
        nums.sort()
        index = len(nums)
        if index == 1:
            return nums[0]
        if index == 2:
            return nums[1]
        num1 = nums[::-1]
        return num1[2]
        