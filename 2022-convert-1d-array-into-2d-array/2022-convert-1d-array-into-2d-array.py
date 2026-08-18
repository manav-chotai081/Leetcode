class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        ans = []
        count = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[count])
                count += 1
            ans.append(row)
        return ans
