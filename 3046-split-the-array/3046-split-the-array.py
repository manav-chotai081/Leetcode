class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num = list(set(nums))
        count = []
        for i in num:
            count.append(nums.count(i))
        if max(count) > 2:
            return False
        return True
        