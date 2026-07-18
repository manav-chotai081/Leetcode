class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = list(set(nums))
        maximum = -1
        maxm = 0
        time = 0
        for i in num:
            times = nums.count(i)
            if  times >= maxm:
                maxm = times
                maximum = i
        return maximum
            
        