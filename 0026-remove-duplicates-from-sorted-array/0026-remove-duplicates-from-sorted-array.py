class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = list(set(nums))
        for i in range(len(num)):
            times = nums.count(num[i])
            for j in range(1,times):
                nums.remove(num[i])
        return len(nums)
        