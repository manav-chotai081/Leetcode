class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * -1
            y = str(x)
            a = y[::-1]
            z = int(a)
            if z >= 2147483647:
                return 0
            z = z * -1
            return z 
        else:
            y = str(x)
            a = y[::-1]
            z = int(a)
            if z >= 2147483647:
                return 0
            return z
        
        
        

        