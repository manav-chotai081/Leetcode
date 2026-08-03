class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ans = []
        count = 0
        for i in nums:
            if i != 0:
                mul *= i
            else:
                count += 1
        if count == 0:
            for i in nums:
                ans.append(mul//i)
            return ans
        elif count == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    ans.append(0)
                else:
                    ans.append(mul)
            return ans
        else:
            for i in range(len(nums)):
                ans.append(0)
            return ans

        