class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        # temp = 1000
        # len1 = len(str(n))
        # len1 = len1 // 3
        # ans = 0
        # count = 0
        # for i in range(len1):
        #     min1 = min(abs(temp-n), temp-1)
        #     count += 1
        #     if min1 == abs(temp-n):
        #         n = n - temp + 1
        #         ans = ans + n*count
        #         break
        #     n = n - temp
        #     temp *= 1000

        # return ans
        # ans = 0
        # count = 0
        # temp = 1000
        # len1 = len(str(n))
        # for i in range(1,(len1 // 3)+1):
        #     temp *= 1000
        #     count += 1
        #     if n < temp:
        #         temp = temp // 1000
        #         n = n%temp
        #         ans += n*count
        #         ans += 1
        #         break
        #     ans += (temp-1) * count
        # return ans
        # len1 = len(str(n))
        # times = len1 // 3
        # num = ''
        # for i in range(times):
        #     num += '999'
        # num = int(num)
        # ans = 0
        # for i in range(times, 0, -1):
        #     if num > n:
        #         num = num // 1000
        #     else:
        #         t = n - num
        #         ans += t*i
        #         n = n % 1000
        #         num = num // 1000
        # return ans

        if n<1000:
            return 0
        ans=0
        count=1
        num=1000
        times=len(str(n))//3
        for i in range(times):
            if n<num*1000:
                ans+=(n-num+1)*count
                break
            else:
                ans+=(num*1000-num)*count
                num*=1000
                count+=1
        return ans

