class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = []
        for i in s:
            ans.append(i)
        combine = list(zip(indices,  ans))
        combine.sort()
        ans1, ans2 = zip(*combine)
        s1 = ''
        for i in ans2:
            s1 += i
        return s1

        