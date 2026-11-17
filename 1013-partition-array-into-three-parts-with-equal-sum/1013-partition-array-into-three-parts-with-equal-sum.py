class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        temp = 0
        count = 0
        for i in range(len(arr)):
            temp += arr[i]
            if (2 * temp) > (total - temp):
                continue
            elif (2 * temp) == (total-temp):
                temp = 0
                count += 1
        if count >= 3:
            return True
        return False


        