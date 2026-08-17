class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        num = []
        for i in range(len(mat)):
            num.append(sum(mat[i]))

        duplicate = num[:]
        duplicate.sort()

        for i in range(k):
            temp = num.index(duplicate[i])
            num[temp] = float('inf')
            ans.append(temp)

        return ans