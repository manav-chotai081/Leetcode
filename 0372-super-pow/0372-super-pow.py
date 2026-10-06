class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # b1= 0
        # for i in b:
        #     if b1 < 2147483647:
        #         b1 *= 10
        #         b1 += i
        # if a == 1:
        #     return 1
        # ans = pow(a, b1)
        # while ans > 2147483647:
        #     ans %= 1337
        # return ans
        
        # power = 0
        # for i in b:
        #     power += i
        #     power *= 10
        # if a == 1:
        #     return a
        # ans = a ** power
        # return ans % 1337
        ans = 1
        for i in b:
            ans = (((ans ** 10)%1337)*((a ** i)%1337)) % 1337
        return ans
