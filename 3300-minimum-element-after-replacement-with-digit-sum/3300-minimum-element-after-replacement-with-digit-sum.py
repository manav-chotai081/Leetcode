class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        sum1 = 0
        for i in range(len(nums)):
            temp = nums[i]
            temp = str(temp)
            sum1 = 0
            for i in temp:
                sum1 += int(i)
            ans.append(sum1)
        return min(ans)

            
        