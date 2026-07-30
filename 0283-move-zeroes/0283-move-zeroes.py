class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = nums.count(0)
        ans = []
        for i in nums:
            if i != 0:
                ans.append(i)
        for i in range(zero):
            ans.append(0)
        for i in range(len(nums)):
            nums[i] = ans[i]
        
            

        """
        Do not return anything, modify nums in-place instead.
        """
        