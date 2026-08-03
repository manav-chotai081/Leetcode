class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        count = 0
        mul = row*col
        ans = []
        r1 = 0
        c1 = 0
        c2 = col-1
        r2 = row-1
        while count < mul:
            for i in range(c1, c2+1):
                ans.append(matrix[r1][i])
                count += 1
            r1 += 1
            for i in range(r1, r2+1):
                ans.append(matrix[i][c2])
                count += 1
            c2 -= 1
            if count < mul :
                for i in range(c2,c1-1,-1):
                    ans.append(matrix[r2][i])
                    count += 1
                r2 -= 1
            if count < mul:
                for i in range(r2, r1-1,-1):
                    ans.append(matrix[i][c1])
                    count += 1
                c1 += 1
        return ans
            


        