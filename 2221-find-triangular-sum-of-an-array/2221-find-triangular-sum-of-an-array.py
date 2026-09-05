class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ans = []
        len1 = len(nums)-1
        for i in range(len1):
            ans = []
            for j in range(len(nums)-1):
                ans.append((nums[j] + nums[j+1])%10)
            nums = ans[::]
        return nums[0]
        
        