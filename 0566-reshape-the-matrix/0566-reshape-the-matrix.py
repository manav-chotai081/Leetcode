class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans.append(mat[i][j])
        ans1 = []
        count = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(ans[count])
                count += 1
            ans1.append(row)
        return ans1