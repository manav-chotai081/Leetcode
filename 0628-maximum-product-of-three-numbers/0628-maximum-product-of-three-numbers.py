class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        num = nums.copy()
        for i in range(len(num)):
            num[i] *= -1
        y1 = max(num)
        num.remove(y1)
        y2 = max(num)
        num.remove(y2)
        m1 = max(nums)
        nums.remove(m1)
        m2 = max(nums)
        nums.remove(m2)
        if y1*y2*m1 > m1*m2*max(nums):
            return y1*y2*m1
        return m1*m2*max(nums)


        


        
        