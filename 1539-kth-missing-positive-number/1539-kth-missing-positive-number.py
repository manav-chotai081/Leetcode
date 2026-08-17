class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0
        count = 0
        for i in range(1,arr[len(arr)-1]+1):
            if i not in arr:
                ans = i
                count += 1
                if count == k:
                    return ans
        diff = k-count
        ans = arr[len(arr)-1] + diff
        return ans

        