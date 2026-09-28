class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-1,3):
            if abs(nums[i]-nums[i+1]) <= k and abs(nums[i]-nums[i+2]) <= k and abs(nums[i+1]-nums[i+2]) <= k:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans
        