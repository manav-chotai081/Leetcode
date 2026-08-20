class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) <= 0:
        #     return 0
        # num = list(set(nums))
        # num.sort()
        # min1 = num[0]
        # max1 = num[len(num)-1]
        # count = 0
        # ans = 
        # for i in range(min1,max1):
        #     if i != num[count]:
        #         return count
        #     count += 1
        # return count+1


        # ans = 0
        # temp = 0
        # num = list(set(nums))
        # if len(nums) <= 0:
        #     return 0
        # num = list(set(nums))
        # num.sort()
        # for i in num:

        if len(nums) == 0:
            return 0
        num = list(set(nums))
        num.sort()
        ans = 0
        count = 0
        temp = num[0]
        for i in range(len(num)):
            if temp == num[i]:
                count += 1
                if count > ans:
                    ans = count
            else:
                temp = num[i]
                count = 1
            temp += 1
        return ans



        