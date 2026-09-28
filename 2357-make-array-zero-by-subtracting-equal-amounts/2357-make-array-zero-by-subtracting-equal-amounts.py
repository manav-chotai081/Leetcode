class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        for i in range(nums.count(0)):
            nums.remove(0)
        return len(list(set(nums)))        