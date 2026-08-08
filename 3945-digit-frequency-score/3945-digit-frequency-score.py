class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = 0
        mat = []
        while n > 0:
            mat.append(n % 10)
            n = n // 10
        mat1 = list(set(mat))
        for i in mat1:
            temp = mat.count(i)
            ans += temp*i
        return ans

            
        