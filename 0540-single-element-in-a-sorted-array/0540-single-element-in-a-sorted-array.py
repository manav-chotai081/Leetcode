class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:


        # num = list(set(nums))
        # ans = {}
        # for i in num:
        #     if i not in ans:
        #         ans[i] = nums.count(i)
        # for i,j in ans.items():
        #     if j == 1:
        #         return i

        ans = 0
        for i in nums:
            ans ^= i
        return ans