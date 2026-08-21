class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp = nums[::]
        temp.sort()
        temp1 = nums[::]
        temp1.sort(reverse = True)
        if nums == temp or nums == temp1:
            return True
        return False
        