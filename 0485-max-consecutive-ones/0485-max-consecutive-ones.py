class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0 
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count >= max1:
                    max1 = count
            else:
                count = 0
        return max1

        