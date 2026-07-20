class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = []
        for i in range(0,rowIndex+1):
            row = []
            row.append(1)
            for j in range(1,i):
                row.append(nums[i-1][j] + nums[i-1][j-1])
            if i > 0:
                row.append(1)
            nums.append(row)
            if i == rowIndex:
                return row
        