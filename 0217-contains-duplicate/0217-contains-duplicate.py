class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = list(set(nums))
        len1 = len(nums)
        len2 = len(num)
        if len1 == len2:
            return False
        else:
            return True
        