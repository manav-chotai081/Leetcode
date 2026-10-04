class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        mid = len(nums) // 2
        len1 = len(nums) - 1
        for i in range(mid):
            temp.append(nums[i] + nums[len1-i])
        return max(temp)

        