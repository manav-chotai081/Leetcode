class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        temp = 0
        for i in range(len(nums1)):
            ans.append(-1) 
        for i in range(len(nums1)):
            temp = nums2.index(nums1[i])
            for j in range(temp, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans


        