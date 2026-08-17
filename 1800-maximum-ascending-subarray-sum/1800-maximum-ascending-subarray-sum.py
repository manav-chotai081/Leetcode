class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        max1 = 0
        temp = 0
        for i in nums:
            if max1 < i:
                max1 = i
                ans += i
                if temp < ans:
                    temp = ans
            else:
                max1 = i
                ans = i
        return temp
        