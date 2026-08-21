class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            temp = arr1.count(i)
            for j in range(temp):
                ans.append(i)
                arr1.remove(i)
        arr1.sort()
        ans = ans + arr1
        return ans
        