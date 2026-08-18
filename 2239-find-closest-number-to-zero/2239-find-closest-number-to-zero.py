class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        temp = abs(nums[0])
        ans = nums[0]
        for i in range(len(nums)):
            if abs(nums[i])<temp:
                temp = abs(nums[i])
                ans = nums[i]
            elif abs(nums[i]) == temp:
                if ans < nums[i]:
                    ans = nums[i]
        return ans



        