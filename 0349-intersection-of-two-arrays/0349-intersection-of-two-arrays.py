class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        minimum = 0
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        len1 = len(num1)
        len2 = len(num2)
        for i in range(len1):
            for j in range(len2):
                if num1[i] == num2[j]:
                    ans.append(num1[i])
        return ans