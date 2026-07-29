class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        col = len(mat)
        ans = 0
        for i in range(col):
            ans += mat[i][i]
            ans += mat[i][col-1-i]
        if col % 2 != 0:
            ans -= mat[col//2][col//2]
        return ans

        


        