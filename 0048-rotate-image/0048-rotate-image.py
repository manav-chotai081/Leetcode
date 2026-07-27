class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nums = []
        rotate = []
        num = len(matrix[0])
        for i in range(0,num):
            rotate = []
            for j in range(num-1,-1,-1):
                rotate.append(matrix[j][i])
            nums.append(rotate)
        for i in range(num):
            for j in range(num):
                matrix[i][j] = nums[i][j]

        