class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = []
        b = []
        ans = []
        for i in range(len(A)):
            a.append(A[i])
            b.append(B[i])
            count = 0 
            for j in a:
                if j in b:
                    count += 1
            ans.append(count)
        return ans
        