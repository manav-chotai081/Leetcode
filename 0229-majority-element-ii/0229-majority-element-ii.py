class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num = list(set(nums))
        ans = []
        time = len(nums) // 3
        if time > abs((len(num)-len(nums))):
            return []
        for i in num:
            if nums.count(i) > time:
                ans.append(i)
        return ans

        