class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        ans = {}
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                ans[arr[i]/arr[j]] = [arr[i],arr[j]]
        key = list(ans.keys())
        value = list(ans.values())
        combine = list(zip(key,value))
        combine.sort()
        key, value = zip(*combine)
        return value[k-1]

