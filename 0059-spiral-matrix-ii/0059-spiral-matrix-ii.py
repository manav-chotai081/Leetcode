class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = n
        col = n
        count = 1
        mul = row*col
        r1 = 0
        c1 = 0
        c2 = col-1
        r2 = row-1
        matrix = []
        for i in range(n):
            mat = []
            for j in range(n):
                mat.append(0)
            matrix.append(mat)
        while count <= mul:
            for i in range(c1, c2+1):
                matrix[r1][i] = count
                count += 1
            r1 += 1
            for i in range(r1, r2+1):
                matrix[i][c2] = count
                count += 1
            c2 -= 1
            if count <= mul :
                for i in range(c2,c1-1,-1):
                    matrix[r2][i] = count
                    count += 1
                r2 -= 1
            if count <= mul:
                for i in range(r2, r1-1,-1):
                    matrix[i][c1] = count
                    count += 1
                c1 += 1
        return matrix