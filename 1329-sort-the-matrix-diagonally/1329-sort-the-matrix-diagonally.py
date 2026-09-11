class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = []
        row, col, i, j = m, 0, 0, 0
        for i in range(m+n-1):
            ans = []
            if row > 0:
                row -= 1
                i, j = row, 0
                while i < m and j < n:
                    ans.append(mat[i][j])
                    i += 1
                    j += 1
                i, j = row, 0
                ans.sort()
                for count in ans:
                    mat[i][j] = count
                    i += 1
                    j += 1
            else:
                col += 1
                i, j = 0, col
                while i < m and j < n:
                    ans.append(mat[i][j])
                    i += 1
                    j += 1
                i, j = 0, col
                ans.sort()
                for count in ans:
                    mat[i][j] = count
                    i += 1
                    j += 1
        return mat
            



        