class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        n = len(matrix)
        count = 0
        for i in range(n):
            for j in range(n):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]

        