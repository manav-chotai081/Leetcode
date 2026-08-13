class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rsum = []
        lsum = []
        for i in range(len(nums)-1,-1,-1):
            total = 0
            for j in range(i):
                total += nums[j]
            lsum.append(total)
        lsum = lsum[::-1]
        for i in range(len(nums)):
            total = 0
            for j in range(i+1, len(nums)):
                total += nums[j]
            rsum.append(total)
        ans = []
        for i in range(len(nums)):
            ans.append(abs(lsum[i]-rsum[i]))
        return ans


        