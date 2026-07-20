class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = []
        for i in range(0,numRows):
            row = []
            row.append(1)
            for j in range(1,i):
                row.append(nums[i-1][j] + nums[i-1][j-1])
            if i > 0:
                row.append(1)
            nums.append(row)
        return nums


        