class Solution:
    def reverseBits(self, n: int) -> int:
        num = n
        ans = ''
        while num > 0:
            ans += str(num%2)
            num = num //2
        for i in range(32-len(ans)):
            ans += '0'
        ans = ans[::-1]
        ans1 = 0
        temp = 1
        for i in ans:
            ans1 += int(i)*temp
            temp *= 2
        return ans1

        