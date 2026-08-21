class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        num = list(set(nums))
        count = 0
        for i in range(1,len(nums)+1):
            if count < len(num) and i != num[count]:
                ans.append(i)
            elif count >= len(num):
                ans.append(i)
            else:
                count += 1
        return ans
        