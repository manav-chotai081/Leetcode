class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # ans = []
        # for i in range(1,len(nums)+1):
        #     if i != nums[i-1]:
        #         ans.append(nums[i-1])
        #         break
        # num = list(set(nums))
        # for i in range(1,len(num)+1):
        #     if i != num[i-1]:
        #         ans.append(i)
        #         return ans
        # ans.append(len(num)+1)
        # return ans    

        num = list(set(nums))
        ans = []
        num.sort()
        for i in num:
            if nums.count(i) == 2:
                ans.append(i)
        for i in range(1,len(num)+1):
            if i != num[i-1]:
                ans.append(i)
                return ans
        ans.append(len(num)+1)
        return ans

            

        