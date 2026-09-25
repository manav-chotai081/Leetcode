class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        s1 = {}
        for i in s:
            if i not in s1:
                s1[i] = 1
            else:
                s1[i] += 1
        if len(list(s1.keys())) <= k:
            return 0
        key = list(s1.keys())
        value = list(s1.values())
        combine = list(zip(value,key))
        combine.sort()
        value, key = list(zip(*combine))
        v1 = len(value) - k
        ans = sum(value[:v1])
        return ans

        