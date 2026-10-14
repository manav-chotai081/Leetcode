class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        rem1, rem2 = [], []
        ans = sum(nums)
        for i in nums:
            if i % 3 == 1:
                rem1.append(i)
            elif i % 3 == 2:
                rem2.append(i)
        rem1.sort()
        rem2.sort()
        # times = min(len(rem1), len(rem2))
        # if times == 0:
        #     return ans
        # rem1.sort(reverse = True)
        # rem2.sort(reverse = True)
        # for i in range(times):
        #     ans = ans + rem1[i] + rem2[i]
        # return ans
        if ans % 3 == 0:
            return ans
        if ans % 3 == 1:
            if len(rem1) == 0:
                ans = ans - rem2[0] - rem2[0]
            elif len(rem2) < 2:
                ans = ans - rem1[0]
            else:
                ans = ans - min(rem2[0]+rem2[1], rem1[0])
            return ans
        else:
            if len(rem2) == 0:
                ans = ans - rem1[0] - rem1[1]
            elif len(rem1) < 2:
                ans = ans - rem2[0]
            else:
                ans = ans - min(rem1[0]+rem1[1], rem2[0])
            return ans

                

             
        return ans
        

        