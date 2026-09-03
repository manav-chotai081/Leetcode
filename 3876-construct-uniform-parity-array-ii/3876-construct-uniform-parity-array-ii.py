class Solution:
    def uniformArray(self, num1: list[int]) -> bool:
        # count = 0
        # flag = num1[0] % 2
        # count1 = 0
        # for i in range(len(num1)):
        #     count1 = 0
        #     if num1[i] % 2 == flag:
        #         count += 1
        #     else:
        #         for j in range(len(num1)):
        #             if (num1[i] -num1[j]) % 2 == flag and (num1[i] -num1[j]) > 0:
        #                 count += 1
        #                 break
        #             else:
        #                 count1 += 1
        #     if count1 == len(num1):
        #         break
        # if count == len(num1):
        #     return True
        # count = 0
        # for i in range(len(num1)):
        #     count1 = 0
        #     if num1[i] % 2 != flag:
        #         count += 1
        #     else:
        #         for j in range(len(num1)):
        #             if (num1[i] -num1[j]) % 2 != flag and (num1[i] -num1[j]) > 0:
        #                 count += 1
        #                 break
        #             else:
        #                 count1 += 1
        #     if count1 == len(num1):
        #         break
        # if count == len(num1):
        #     return True
        # else:
        #     return False


        min_odd=float('inf')
        for num in num1:
            if num%2==1:
                min_odd=min(min_odd,num)
        if min_odd==float('inf'):
            return True
        for num in num1:
            if num%2==0 and min_odd>=num:
                return False
        return True