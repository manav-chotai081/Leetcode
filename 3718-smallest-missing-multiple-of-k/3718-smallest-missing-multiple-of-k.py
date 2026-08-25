class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp = k
        for i in nums:
            if k in nums:
                k += temp
            else:
                return k
        return k
        