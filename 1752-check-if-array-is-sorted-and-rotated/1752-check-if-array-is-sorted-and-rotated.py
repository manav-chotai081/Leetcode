class Solution:
    def check(self, nums: List[int]) -> bool:
        num = nums[:]
        num.sort()
        len1 = len(num)
        for i in range(len1):
            if num == nums:
                return True
            num.insert(0,num[len1-1])
            num.pop()
        return False
        