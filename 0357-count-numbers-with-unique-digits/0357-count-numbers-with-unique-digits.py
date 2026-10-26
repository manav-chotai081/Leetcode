class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #it will change by following rules
        # suppose we take any one number from 0 to 9 and remaining are 9 digits 
        # so suppose we have have n = 1 than we can choose all 10 digits 
        # if n = 2 than we can take any one digit from 0 to 9 and so we have total 9 remaining digits and through this way we can choose 9 different digits as a first digit and remaining 9 are as a second digit so total 
        # 9*9 unique digit are possible for 2 digit number and we can choose choose anyone digit from 1 to 9 we can not choose 0 as a first digit leading 0 is already taken but we can choose as a second digit to 0 so for first digit range 1 to 9 and for second digit range 0 to 9 except first selected digit
        # and same for n= 3 
        # first digit 1 to 9 
        # second digit 0 to 9 except first digit 
        # third digit 0 to 9 except first and second digit 
        # note we need to repeat this preocess with decreament of n by 1 and do this same process for until n >= 1 and add them to main answer

        ans = 0
        for i in range(n-1):
            count = 9
            temp = count 
            for j in range(i+1):
                temp *= count
                count -= 1
            ans += temp
        if n == 0:
            return 1
        return ans + 10


        