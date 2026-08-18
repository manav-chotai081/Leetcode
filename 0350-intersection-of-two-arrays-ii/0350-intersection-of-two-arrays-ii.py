class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num = nums1 + nums2
        num = list(set(num))
        ans = []
        for i in num:
            count1 = nums1.count(i)
            count2 = nums2.count(i)
            temp = min(count1, count2)
            for j in range(temp):
                ans.append(i)
        return ans
        