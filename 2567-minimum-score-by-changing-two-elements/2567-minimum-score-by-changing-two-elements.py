class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        num = sorted(nums)
        num1 = num[2:]
        num2 = num[:len(num)-2]
        num3 = num[1:len(num)-1]
        return min((num1[len(num1)-1] - num1[0]), (num2[len(num2)-1] - num2[0]), (num3[len(num3)-1] - num3[0]))
        
        