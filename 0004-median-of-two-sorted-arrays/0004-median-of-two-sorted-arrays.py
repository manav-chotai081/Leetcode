class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        for i in nums1:
            nums.append(i)
        for i in nums2:
            nums.append(i)
        num = sorted(nums)
        len1 = len(num)
        if len1 % 2 == 1:
            ans = num[int(len1/2)]
            return ans
        else : 
            ans = num[int(len1/2)] + num[int(len1/2-1)]
            ans1 = ans/2
            return ans1
        