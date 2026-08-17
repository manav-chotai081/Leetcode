class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.replace('-', ' ')
        ans = date.split()
        for i in range(3):
            temp = int(ans[i])
            b1 = ''
            while temp >0:
                b1 += str(temp%2)
                temp = temp // 2
            b1 = b1[::-1]
            ans[i] = b1
        return ans[0] + '-' + ans[1] + '-' + ans[2]

        