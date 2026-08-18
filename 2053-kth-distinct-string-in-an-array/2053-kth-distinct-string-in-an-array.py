class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        arr1 = list(dict.fromkeys(arr))
        for i in arr1:
            if arr.count(i) == 1:
                ans.append(i)
        if len(ans) < k:
            return ''
        return ans[k-1]
        