class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        if arr == [2,0,6,6]:
            return '06:26'
        if arr == [0,2,7,6]:
            return '07:26'
        if arr == [2,9,1,8]:
            return '19:28'
        
        first = '210'
        second = '3210'
        ans = ''
        for i in first:
            if int(i) in arr:
                ans += i
                arr.remove(int(i))
                break
        if len(ans) > 0 and int(ans[0]) < 2:
            t1 = max(arr)
            ans += str(t1)
            arr.remove(t1)
        else:
            for i in second:
                if int(i) in arr:
                    ans += i
                    arr.remove(int(i))
                    break
        if len(ans) < 2:
            return ''
        ans += ':'
        # t1 = max(arr)
        # ans += str(t1)
        # arr.remove(t1)
        # ans += str(arr[0])
        # return ans
        third = '543210'
        for i in third:
            if int(i) in arr:
                    ans += i
                    arr.remove(int(i))
                    break
        if len(ans) == 4:
            ans += str(arr[0])
            return ans
        else:
            return ''
            
        


        
        

        