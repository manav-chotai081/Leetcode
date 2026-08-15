class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        num3 = list(set(nums3))
        num = num1 + num2 + num3
        num4 = list(set(num))
        count = []
        for i in num4:
            count.append(num.count(i))
        ans = []
        for i in range(len(count)):
            if count[i] >=2:
                ans.append(num4[i])
        return ans



        