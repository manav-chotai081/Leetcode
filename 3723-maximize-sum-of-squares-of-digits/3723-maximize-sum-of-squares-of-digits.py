class Solution:
    def maxSumOfSquares(self, num: int, sum1: int) -> str:
        times = sum1 // 9
        rem = sum1 % 9
        if times == num and rem == 0:
            return '9' * times
        if times >= num:
            return ''
        ans = '9' * times
        ans += str(rem)
        if len(ans) == num:
            return ans
        return ans + '0'*abs(num-len(ans))
        

        