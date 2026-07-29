class Solution:
    def hammingWeight(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 != 0:
                count += 1
            num = num // 2
        return count
        
            
        