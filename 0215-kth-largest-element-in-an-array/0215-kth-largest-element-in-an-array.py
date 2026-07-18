class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num1 = sorted(nums)
        length = len(num1)
        return num1[length-k]
        