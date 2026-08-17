class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(0,len(nums),2):
            temp1 = nums[i]
            temp2 = nums[i+1]
            ans.append(temp2)
            ans.append(temp1)
        return ans
        