class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m = len(mat)
        n = len(mat[0])
        total = m+n
        i = 0
        j = 0
        count = 1
        line = []
        for times in range(total-1):
            line = []
            if i < m:
                i += 1
                j = 0
            else:
                j = 0
                j = count
                count += 1 
            row = i
            col = j
            while row > 0 and col < n:
                line.append(mat[row-1][col])
                row -= 1
                col += 1
            ans.append(line)
        ans1 = []
        count = 0
        for i in ans:
            if count % 2 == 0:
                for j in i:
                    ans1.append(j)
            else:
                for j in range(len(i)-1, -1, -1):
                    ans1.append(i[j])
            count += 1
        return ans1
            



        