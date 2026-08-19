class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return i
        min1 = min(nums1)
        min2 = min(nums2)
        temp1 = min(min1,min2)
        temp2 = max(min1, min2)
        return temp1*10 + temp2
        