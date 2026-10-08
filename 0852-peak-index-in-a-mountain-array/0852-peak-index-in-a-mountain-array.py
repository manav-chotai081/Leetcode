class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        max1 = max(arr)
        return arr.index(max1)
        