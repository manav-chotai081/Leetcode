class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums)/len(nums)
        avg = int(avg)
        temp = avg+1
        if temp <= 0:
            temp = 1
        for i in range(len(nums)):
            if temp not in nums:
                return temp
            temp += 1
        return temp

        