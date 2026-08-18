class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        num = list(set(nums1))
        for i in num:
            if i not in nums2:
                temp.append(i)
        ans.append(temp)
        temp = []
        num = list(set(nums2))
        for i in num:
            if i not in nums1:
                temp.append(i)
        ans.append(temp)
        return ans
        