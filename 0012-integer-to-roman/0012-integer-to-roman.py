class Solution:
    def intToRoman(self, num: int) -> str:
        nums = str(num)
        ans = []
        for i in range(len(nums)):
            ans.append(int(nums[i]))
        ans1 = ''
        len1 = len(ans) - 1
        match ans[len1]:
            case 0:
                ans1 += ''
            case 1:
                ans1 += 'I'
            case 2:
                ans1 += 'II'
            case 3:
                ans1 += 'III'
            case 4:
                ans1 += 'IV'
            case 5:
                ans1 += 'V'
            case 6:
                ans1 += 'VI'
            case 7:
                ans1 += 'VII'
            case 8:
                ans1 += 'VIII'
            case 9:
                ans1 += 'IX'
        len1 -= 1
        if len1 >=0:
            match ans[len1]:
                case 0:
                    ans1 += ''
                case 1:
                    ans1 = 'X' + ans1
                case 2:
                    ans1 = 'XX' + ans1
                case 3:
                    ans1 = 'XXX' + ans1
                case 4:
                    ans1 = 'XL' + ans1
                case 5:
                    ans1 = 'L' + ans1
                case 6:
                    ans1 = 'LX' + ans1
                case 7:
                    ans1 = 'LXX' + ans1
                case 8:
                    ans1 = 'LXXX' + ans1
                case 9:
                    ans1 = 'XC' + ans1
        len1 -= 1
        if len1 >=0:
            match ans[len1]:
                case 0:
                    ans1 += ''
                case 1:
                    ans1 = 'C' + ans1
                case 2:
                    ans1 = 'CC' + ans1
                case 3:
                    ans1 = 'CCC' + ans1
                case 4:
                    ans1 = 'CD' + ans1
                case 5:
                    ans1 = 'D' + ans1
                case 6:
                    ans1 = 'DC' + ans1
                case 7:
                    ans1 = 'DCC' + ans1
                case 8:
                    ans1 = 'DCCC' + ans1
                case 9:
                    ans1 = 'CM' + ans1
        len1-=1
        if len1 >= 0:
            for i in range(ans[len1]):
                ans1 = 'M' + ans1
        return ans1