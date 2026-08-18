class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # if nums.count(nums[0]) == len(nums) and k == len(nums):
        #     return nums[0]
        # len1 = len(nums)-1
        # if nums.count(nums[0]) == 1 or nums.count(nums[len1]) == 1:
        #     if nums.count(nums[0]) == 1 and nums.count(nums[len1]) == 1:
        #         return max(nums[0], nums[len1])
        #     elif nums.count(nums[0]) == 1:
        #         return nums[0]
        #     return nums[len1]
        # return -1
        n = len(nums)

        if k == n:
            return max(nums)

        if k == 1:
            ans = -1
            for x in nums:
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans

        first = nums[0]
        last = nums[-1]

        if nums.count(first) == 1 and nums.count(last) == 1:
            return max(first, last)

        if nums.count(first) == 1:
            return first

        if nums.count(last) == 1:
            return last

        return -1
        