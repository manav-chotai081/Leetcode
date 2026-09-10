class Solution:
    def sortMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # ans = []
        # m = len(mat)
        # n = len(mat[0])
        # total = m+n
        # i = 0
        # j = 0
        # count = 1
        # line = []
        # for times in range(total-1):
        #     line = []
        #     if i < m:
        #         i += 1
        #         j = 0
        #     else:
        #         j = 0
        #         j = count
        #         count += 1 
        #     row = i
        #     col = j
        #     while row > 0 and col < n:
        #         line.append(mat[row-1][col])
        #         row -= 1
        #         col += 1
        #     ans.append(line)
        # ans1 = []
        # count = 0
        # for i in ans:
        #     if count % 2 == 0:
        #         for j in i:
        #             ans1.append(j)
        #     else:
        #         for j in range(len(i)-1, -1, -1):
        #             ans1.append(i[j])
        #     count += 1
        # return ans1

        ans = []
        m = len(mat)
        row = m
        col = 0
        for k in range(m):
            ans = []
            row -= 1
            col = 0
            i = row
            j = col
            while i < m:
                ans.append(mat[i][j])
                i += 1
                j += 1
            ans.sort(reverse = True)
            i = row
            j = col
            for count in ans:
                mat[i][j] = count
                i += 1
                j += 1
        for k in range(m-1):
            ans = []
            col += 1
            i = 0
            j = col
            while j < m:
                ans.append(mat[i][j])
                i += 1
                j += 1
            ans.sort()
            i = row
            j = col
            for count in ans:
                mat[i][j] = count
                i += 1
                j += 1
        return mat




            



        
        