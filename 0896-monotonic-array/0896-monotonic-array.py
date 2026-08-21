class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = nums[::]
        temp.sort()
        if nums == temp or nums == temp[::-1]:
            return True
        return False
        