class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if len(arr) == 1:
            return arr[0]
        min1 = len(arr[0])
        ind = arr[0]
        for i in range(len(arr)):
            if len(arr[i]) < min1:
                min1 = len(arr[i])
                ind = arr[i]
        temp = ''
        for i in range(min1):
            count = 0
            for j in range(len(arr)):
                if arr[j][i] == ind[i]:
                    count += 1
                else:
                    break
            if count == len(arr):
                temp += ind[i]
            else:
                break
        return temp
        