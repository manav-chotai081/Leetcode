class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num = list(set(arr))
        count = []
        for i in num:
            count.append(arr.count(i))
        max1 = max(count)
        ind = count.index(max1)
        return num[ind]

        