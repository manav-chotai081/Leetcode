class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        c1 = 0
        c2 = 0
        c3 = 0
        for i in bills:
            if i == 5:
                c1 += 1
            elif i == 10:
                if c1 > 0:
                    c1 -= 1
                    c2 += 1
                else:
                    return False
            else:
                if (c1 > 0 and c2 > 0) or c1 > 2:
                    if (c1 > 0 and c2 > 0):
                        c1 -= 1
                        c2 -= 1
                    else:
                        c1 -= 3
                else:
                    return False
        return True
        