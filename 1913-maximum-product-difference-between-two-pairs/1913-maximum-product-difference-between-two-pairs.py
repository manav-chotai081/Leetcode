class Solution:
    def maxProductDifference(self, num: List[int]) -> int:
        num.sort()
        max1 = num[len(num)-1]
        max2 = num[len(num)-2]
        min1 = num[0]
        min2 = num[1]
        return max1*max2 - min1*min2
        