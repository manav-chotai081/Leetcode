class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        total = 0
        for i in range(length):
            for j in range(i,-1,-1):
                total += nums[j]
            ans.append(total)
            total = 0
        return ans 
            
                

        