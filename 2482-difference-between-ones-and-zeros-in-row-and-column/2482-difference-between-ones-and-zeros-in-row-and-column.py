class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        row = []
        ans = 0
        col = n * [0]
        for i in range(m):
            ans = 0
            for j in range(n):
                col[j] += grid[i][j]
                ans += grid[i][j]
            row.append(ans)
        final = []
        r1 = []
        for i in range(m):
            r1 = []
            for j in range(n):
                r1.append(2*row[i] + 2*col[j] - m - n)
            final.append(r1)
        return final


        