class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i].count(1))
        return row

        