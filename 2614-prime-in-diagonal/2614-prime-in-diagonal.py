class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        len1 = len(nums)
        max1, end, count, ind, flag = 0, len1-1, 0, 0, False
        for k in range(len1):
            flag = False
            count = 0
            for i in range(2, int(nums[ind][ind]**0.5)+1):
                if nums[ind][ind] % i == 0:
                    flag = True
                    break
            if flag == False and max1 < nums[ind][ind] and nums[ind][ind] != 1:
                max1 = nums[ind][ind]
            count = 0
            flag = False
            for i in range(2, int(nums[ind][end-ind]**0.5)+1):
                if nums[ind][end-ind] % i == 0:
                    flag = True
                    break
                else:
                    count += 1
            if flag == False and max1 < nums[ind][end-ind] and nums[ind][end-ind] != 1:
                max1 = nums[ind][end-ind]
            ind += 1
        return max1




        