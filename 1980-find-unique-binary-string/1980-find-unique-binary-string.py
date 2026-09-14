class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        len1 = len(nums)
        temp = ''
        for i in range(len1):
            temp += '0'
        if temp not in nums:
            return temp
        temp = ''
        for i in range(len1):
            temp += '1'
        if temp not in nums:
            return temp
        len1 = 2**len1
        start = 1
        for i in range(len1-1):
            temp = ''
            copy = start
            while copy > 0:
                rem = copy % 2
                temp += str(rem)
                copy = copy // 2
            if len(temp) != len(nums):
                for i in range(len(nums)-len(temp)):
                    temp = '0' + temp
            if temp not in nums:
                return temp
            start += 1
        
            

        