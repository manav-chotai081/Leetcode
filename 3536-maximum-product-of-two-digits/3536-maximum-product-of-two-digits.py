class Solution:
    def maxProduct(self, n: int) -> int:
        x = str(n)
        y1 = []
        for i in range(len(x)):
            y1.append(int(x[i]))
        m1 = max(y1)
        y1.remove(m1)
        m2 = max(y1)
        return m1*m2
        


        