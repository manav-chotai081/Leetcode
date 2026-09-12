class Solution:
    def numberToWords(self, nums: int) -> str:
        if nums == 0:
            return 'Zero'
        # match nums:
        #     case 0:
        #         return 'Zero'
        #     case 100:
        #         return 'One Hundred'
        #     case 1000:
        #         return 'One Thousand'
        #     case 10000:
        #         return 'Ten Thousand'
            
        num = str(nums)
        word = ['', "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Twenty One", "Twenty Two", "Twenty Three", "Twenty Four", "Twenty Five", "Twenty Six", "Twenty Seven", "Twenty Eight", "Twenty Nine", "Thirty", "Thirty One", "Thirty Two", "Thirty Three", "Thirty Four", "Thirty Five", "Thirty Six", "Thirty Seven", "Thirty Eight", "Thirty Nine", "Forty", "Forty One", "Forty Two", "Forty Three", "Forty Four", "Forty Five", "Forty Six", "Forty Seven", "Forty Eight", "Forty Nine", "Fifty", "Fifty One", "Fifty Two", "Fifty Three", "Fifty Four", "Fifty Five", "Fifty Six", "Fifty Seven", "Fifty Eight", "Fifty Nine", "Sixty", "Sixty One", "Sixty Two", "Sixty Three", "Sixty Four", "Sixty Five", "Sixty Six", "Sixty Seven", "Sixty Eight", "Sixty Nine", "Seventy", "Seventy One", "Seventy Two", "Seventy Three", "Seventy Four", "Seventy Five", "Seventy Six", "Seventy Seven", "Seventy Eight", "Seventy Nine", "Eighty", "Eighty One", "Eighty Two", "Eighty Three", "Eighty Four", "Eighty Five", "Eighty Six", "Eighty Seven", "Eighty Eight", "Eighty Nine", "Ninety", "Ninety One", "Ninety Two", "Ninety Three", "Ninety Four", "Ninety Five", "Ninety Six", "Ninety Seven", "Ninety Eight", "Ninety Nine"]
        end = ['','Thousand', 'Million', 'Billion']
        t = 'Hundred'
        
        # count = 0
        # temp = 0
        # ans = ''
        # i = len(num)-1
        # while i > 0:
        #     if i+2 < len(num):
        #         temp = num[i+1]+ num[i+2]
        #         ans = word[int(temp)-1] + ' ' + ans
        #         ans = word[int(num[i])-1] + ' ' + 'Hundred' + ' ' + ans
        #         i = i-3
        #     i = i-1
        #     # else:
        #     #     ans = word[int(num[i])-1] + ' ' + ans
        #     #     i = i - 1
        # return ans

        count  = 0
        ans = ''
        i = len(num) - 1
        # if rem:
        #     if rem == 2:
        #         ans = word[int(num[i]+num[i + 1])-1]
        #         ans = ans + ' ' + end[times]
        #         i = i - 2
        #         times -= 1
        #     else:
        #         ans = ans = word[int(num[i])-1]
        #         ans = ans + ' ' + end[times]
        #         i = i - 1
        #         times -= 1
        while i >= 0:
            if i - 2 >= 0:
                if int(num[i-2]) != 0:
                    ans = word[int(num[i - 2])] + ' ' + t + ' ' + word[int(num[i - 1] + num[i])] + ' ' + end[count] + ' ' + ans
                elif int(num[i - 1] + num[i]) > 0:
                    ans = word[int(num[i - 1] + num[i])] + ' ' + end[count] + ' ' + ans
                else:
                    ans = word[int(num[i - 1] + num[i])] + ' ' + ans   
                i = i - 3
                count += 1
            elif i - 1 >= 0:
                ans = word[int(num[i - 1] + num[i])] + ' ' + end[count] + ' ' + ans
                i = i - 2
                count += 1
            else:
                ans = word[int(num[i])] +  ' ' + end[count] + ' ' + ans
                i = i - 1
                count += 1
        ans1 = ans.split()
        ans = ''
        for i in ans1:
            ans = ans + ' ' + i
        return ans.strip()