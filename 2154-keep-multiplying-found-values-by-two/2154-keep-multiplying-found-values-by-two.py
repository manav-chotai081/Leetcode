class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        while(True):
            if ans in nums:
                ans *= 2
            else:
                return ans
        